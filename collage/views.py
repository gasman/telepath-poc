import json
from django.shortcuts import render
from telepath import JSContext

from .shapes import Circle, Rectangle


def index(request):
    shapes = [
        Circle(30, 'red'),
        Circle(50, 'blue'),
        Rectangle(100, 50, 'yellow'),
    ]

    js_context = JSContext()
    shapes_json = json.dumps([
        js_context.pack(shape)
        for shape in shapes
    ])

    return render(request, 'collage/index.html', {
        'shapes_json': shapes_json,
        'media': js_context.media,
    })
