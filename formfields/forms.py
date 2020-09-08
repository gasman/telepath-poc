from django import forms

from wagtail.admin.widgets import AdminPageChooser
from wagtail.core.models import Page

from telepath import register, Adapter


class MyForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    office = forms.ChoiceField(choices=[('charlbury', "Charlbury"), ('bristol', "Bristol")])
    profile_page = forms.ModelChoiceField(queryset=Page.objects.all(), widget=AdminPageChooser(can_choose_root=False))


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


class PageChooserAdapter(Adapter):
    js_constructor = 'formfields.PageChooser'

    def js_args(self, widget, context):
        return [
            widget.render_html('__NAME__', None, attrs={'id': '__ID__'}),
            widget.id_for_label('__ID__'),
            widget.model_names, widget.can_choose_root, widget.user_perms
        ]

    @property
    def media(self):
        return AdminPageChooser().media + forms.Media(js=['formfields/js/widget.js'])

register(PageChooserAdapter(), AdminPageChooser)
