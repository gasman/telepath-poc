from django import forms

adapters = {}

def register(adapter, cls):
    adapters[cls] = adapter


class JSContext:
    def __init__(self):
        self.media = forms.Media(js=['telepath.js'])
        self.objects = {}

    def pack(self, obj):
        for cls in type(obj).__mro__:
            adapter = adapters.get(cls)
            if adapter:
                break

        if adapter is None:
            raise Exception("don't know how to add object to JS context: %r" % obj)

        self.media += adapter.media
        return [adapter.js_constructor, *adapter.js_args(obj)]
