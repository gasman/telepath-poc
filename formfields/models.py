from django.db import models

from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.core.models import Page


class PersonPage(Page):
    other_page = models.ForeignKey(Page, blank=True, null=True, on_delete=models.SET_NULL, related_name='+')

    content_panels = Page.content_panels + [
        PageChooserPanel('other_page'),
    ]
