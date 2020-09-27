import json

from django.shortcuts import render
from telepath import JSContext

from wagtail.core import blocks

from streamfield import blocks as foo  # load adapters


def index(request):
    block = blocks.StructBlock([
        ('first_name', blocks.CharBlock()),
        ('surname', blocks.CharBlock()),
    ])
    block.set_name("title")

    js_context = JSContext()
    block_json = json.dumps(js_context.pack(block))

    value_json = json.dumps("hello world")

    return render(request, 'streamfield/index.html', {
        'media': js_context.media,
        'block_json': block_json,
        'value_json': value_json,
    })
