import json

from django import forms

from telepath import JSContext

class Collage:
    def __init__(self, shapes):
        self.js_context = JSContext()
        self.shape_decls = json.dumps([
            self.js_context.pack(shape)
            for shape in shapes
        ])

    @property
    def media(self):
        return self.js_context.media + forms.Media(js=['collage/js/collage.js'])
