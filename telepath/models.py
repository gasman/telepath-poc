import json

from django.db import models
from django.forms import Media, MediaDefiningClass

from .context import register, JSContext


class Circle:
    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = colour


class CircleAdapter(metaclass=MediaDefiningClass):
    js_constructor = 'shapes.Circle'

    def js_args(self, obj):
        return [obj.radius, obj.colour]

    class Media:
        js = ['shapes/circle.js']

register(CircleAdapter(), Circle)


class Rectangle:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour


class RectangleAdapter(metaclass=MediaDefiningClass):
    js_constructor = 'shapes.Rectangle'

    def js_args(self, obj):
        return [obj.width, obj.height, obj.colour]

    class Media:
        js = ['shapes/rectangle.js']

register(RectangleAdapter(), Rectangle)


class Collage:
    def __init__(self, shapes):
        self.js_context = JSContext()
        self.shape_decls = json.dumps([
            self.js_context.pack(shape)
            for shape in shapes
        ])

    @property
    def media(self):
        return self.js_context.media + Media(js=['collage.js'])
