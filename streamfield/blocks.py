from wagtail.core import blocks
from telepath import register, Adapter

from formfields import forms  # load field adapters


class FieldBlockAdapter(Adapter):
    js_constructor = 'streamfield.FieldBlock'

    def js_args(self, block, context):
        return [
            block.name,
            context.pack(block.field.widget),
            {'label': block.label, 'required': block.required, 'icon': block.meta.icon},
        ]

    class Media:
        js = ['streamfield/js/blocks.js']

register(FieldBlockAdapter(), blocks.FieldBlock)


class StructBlockAdapter(Adapter):
    js_constructor = 'streamfield.StructBlock'

    def js_args(self, block, context):
        return [
            block.name,
            [context.pack(child) for child in block.child_blocks.values()],
            {
                'label': block.label, 'required': block.required, 'icon': block.meta.icon,
                'classname': block.meta.form_classname, 'helpText': getattr(block.meta, 'help_text', None),
            },
        ]

    class Media:
        js = ['streamfield/js/blocks.js']

register(StructBlockAdapter(), blocks.StructBlock)
