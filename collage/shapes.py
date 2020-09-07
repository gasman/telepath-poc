import json

from django.db import models

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


class Rectangle:
    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = colour


class RectangleAdapter(Adapter):
    js_constructor = 'shapes.Rectangle'

    def js_args(self, obj, context):
        return [obj.width, obj.height, obj.colour]

    class Media:
        js = ['collage/js/shapes/rectangle.js']

register(RectangleAdapter(), Rectangle)
