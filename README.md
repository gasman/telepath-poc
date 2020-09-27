# Telepath

a proof-of-concept for bridging Python and Javascript objects

## The problem

see: [RFC 59](https://github.com/wagtail/rfcs/pull/59/files), [#6226](https://github.com/wagtail/wagtail/pull/6226)

react-streamfield relies on being able to perform client-side operations on Django form fields, such as:

* rendering a new instance of a field, prepopulated with a given value
* extracting the value of a field in JSON-serializable format

This is harder than it sounds, because Django guarantees almost nothing about how form widgets behave on the front end. For example:

* they may need to be initialised with Javascript code (e.g. page choosers, Draftail)
* one widget may correspond to multiple HTML form elements with unpredictable IDs (e.g. radio buttons, checkboxes)
* they may have internal state which is not accessible through form element values (e.g. image choosers, where selecting an image updates the thumbnail as well as the hidden ID field)

As a result, react-streamfield has to rely on form fields following certain Wagtail-specific idioms (e.g. Javascript-dependent widgets having an inline `<script>` tag in their rendered HTML), or failing that, has to patch the widget code to fit its own requirements (e.g. for image choosers, setting the ID field triggers an AJAX fetch of the image data). This creates an unreasonably close coupling between react-streamfield and the current form widget implementations.

A more future-proof approach would be for each form widget - the Django default set, as well as Wagtail's custom widgets and any third-party ones - to expose a standard Javascript API for these client-side operations. This way, react-streamfield can manipulate form widgets without having to know about their internal implementation. This API will have other potential uses, too, such as serialising form contents to post to a JSON REST API.

This implies that every instance of Django's Widget class needs a corresponding Javascript object - and since the behaviour of that Javascript object will be determined in part by the Django-side configuration options, we need a mechanism to pass this configuration data from the server-side code to the client side.

## telepath

`telepath` is a tiny library for setting up mappings between Python and Javascript objects. In use, it looks like this (example taken from the `collage` app):

* Define some Python objects

      shapes = [
          Circle(30, 'red'),
          Circle(50, 'blue'),
          Rectangle(100, 50, 'yellow'),
      ]
* Create a `JSContext` object and pass objects to its `pack` method to obtain JSON-serializable representations of those objects

      from telepath import JSContext

      js_context = JSContext()
      shapes_json = json.dumps([
          js_context.pack(shape)
          for shape in shapes
      ])
* Output the resulting JSON on the template somewhere where Javascript code can access it (I suggest a `data-` attribute on an appropriate HTML element), along with `js_context.media`
* Within Javascript code, call `telepath.unpack` on the parsed JSON representation to obtain the final Javascript object

      canvas = document.getElementById('collage');
      var shapes = JSON.parse(canvas.dataset.shapes).map((shapeData) => {
          return telepath.unpack(shapeData);
      });

Things to note:

* All object configuration data is passed in JSON, and the Javascript-side implementation is in static files, so no inline Javascript is required. This saves having to worry about execution order or how to escape the string `</script>` when it appears in data; it also brings us closer to full CSP compliance.
* The logic for setting up the mapping between the Python and Javascript 'shape' objects is external to those classes, so it can be used on object types that aren't part of our codebase, such as Django's built-in form widgets.

(if it wasn't for these factors, we could probably get away without an actual library for this, and just have a convention such as "Python objects must provide a `media` property and a `js_constructor` method that returns a JS expression string evaluating to the Javascript object"...)

## Configuration

A mapping is defined by registering an `Adapter` object for a given Python class; this specifies the file containing the Javascript implementation, a namespaced identifier for the JS constructor function, and a method that returns a list of (JSON-serializable) arguments to be passed to that constructor to recreate a given Python object.

    from telepath import register, Adapter


    class Circle:
        def __init__(self, radius, colour):
            self.radius = radius
            self.colour = colour


    class CircleAdapter(Adapter):
        js_constructor = 'shapes.Circle'

        def js_args(self, obj, context):
            return [obj.radius, obj.colour]

        class Media:
            js = ['collage/js/shapes/circle.js']

    register(CircleAdapter(), Circle)


When packing objects, telepath will check the object's type and select the adapter for the most specific superclass (as defined by `type(obj).__mro__`).

On the Javascript side, the corresponding constructor function is registered under the given identifier, with `telepath.register`.

    class Circle {
        constructor(radius, colour) {
            this.radius = radius;
            this.colour = colour;
        }

        draw(ctx, x, y) {
            ctx.fillStyle = this.colour;
            ctx.beginPath();
            ctx.arc(x, y, this.radius, 0, 2 * Math.PI);
            ctx.fill();
        }
    }

    telepath.register('shapes.Circle', Circle);


## Form widgets

The `formfields` app (accessible at the URL `/forms/`) demonstrates this being used on Django form widget objects. Currently this depends on a patch to Wagtail: [gasman/telepath-streamfield](https://github.com/gasman/wagtail/tree/telepath-streamfield)

The Javascript object corresponding to a `Widget` instance implements a single method `render(placeholder, name, id)`, which replaces the HTML element `placeholder` with a copy of the widget, with the given name and ID, and returns an accessor object with the additional methods:

* `getValue()` - return the submittable value of this form field
* `getState()` - return an object containing all state necessary to replicate this field elsewhere. (Often this will just be the field value, but e.g. an image chooser will also need to include the image thumbnail URL / dimensions, not just the image ID)
* `setState(state)` - set this field to the given state (as per `getState`).
