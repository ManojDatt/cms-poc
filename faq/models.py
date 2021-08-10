from wagtail.core.models import Page
from django.db import models
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

class FAQIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class FAQPage(Page):
    date = models.DateField("Post date", auto_now_add=True, editable=True)
    subject = RichTextField(blank=True)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('subject'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('subject'),
        FieldPanel('body', classname="full"),
    ]