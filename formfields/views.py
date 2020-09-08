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
    form_data = json.dumps({
        'title': "Matthew",
        'description': "just this guy, y'know?",
        'office': "charlbury",
        'profile_page': {
            'id': 3,
            'parentId': 2,
            'title': 'Matthew',
            'editUrl': '/cms/pages/3/',
        },
    })

    return render(request, 'formfields/index.html', {
        'media': js_context.media,
        'widgets': widgets,
        'form_data': form_data,
    })
