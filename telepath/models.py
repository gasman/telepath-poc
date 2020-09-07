import json

from django.db import models
from django.forms import Media, MediaDefiningClass

from .context import register, JSContext


class Circle:
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour


class CircleAdapter(metaclass=MediaDefiningClass):
    # FIXME: json.dumps doesn't escape </script> inside the string
    def jsify(self, obj):
        return "new Circle(%d, %s)" % (obj.radius, json.dumps(obj.colour))

    class Media:
        js = ['shapes/circle.js']

register(CircleAdapter(), Circle)


class Rectangle:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour


class RectangleAdapter(metaclass=MediaDefiningClass):
    def jsify(self, obj):
        return "new Rectangle(%d, %d, %s)" % (obj.width, obj.height, json.dumps(obj.colour))

    class Media:
        js = ['shapes/rectangle.js']

register(RectangleAdapter(), Rectangle)


class Collage:
    def __init__(self, shapes):
        self.js_context = JSContext()
        self.shape_decls = [
            self.js_context.jsify(shape)
            for shape in shapes
        ]

    @property
    def media(self):
        return Media(js=['collage.js']) + self.js_context.media
