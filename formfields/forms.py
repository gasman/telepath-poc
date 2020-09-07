from django import forms

from telepath import register, Adapter


class MyForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    office = forms.ChoiceField(choices=[('charlbury', "Charlbury"), ('bristol', "Bristol")])


class WidgetAdapter(Adapter):
    js_constructor = 'formfields.Widget'

    def js_args(self, widget, context):
        return [
            widget.render('__NAME__', None, attrs={'id': '__ID__'}),
            widget.id_for_label('__ID__'),
        ]

    class Media:
        js = ['formfields/js/widget.js']

register(WidgetAdapter(), forms.widgets.Input)
register(WidgetAdapter(), forms.Textarea)
register(WidgetAdapter(), forms.Select)
