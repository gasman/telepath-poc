import json
from django.shortcuts import render

from telepath import JSContext

from .forms import MyForm


def index(request):
    form = MyForm()

    js_context = JSContext()
    widgets = json.dumps({
        name: js_context.pack(field.widget)
        for name, field in form.fields.items()
    })

    return render(request, 'formfields/index.html', {
        'media': js_context.media,
        'widgets': widgets,
    })
