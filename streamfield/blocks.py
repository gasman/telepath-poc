from wagtail.core.blocks import FieldBlock
from telepath import register, Adapter

from formfields import forms  # load field adapters


class FieldBlockAdapter(Adapter):
    js_constructor = 'streamfield.FieldBlock'

    def js_args(self, block, context):
        return [
            context.pack(block.field.widget),
        ]

    class Media:
        js = ['streamfield/js/blocks.js']

register(FieldBlockAdapter(), FieldBlock)
