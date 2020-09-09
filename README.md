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
