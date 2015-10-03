# coding: utf-8
from django import template
from django.conf import settings
from funcy import ichunks

from gallery.models import Gallery

register = template.Library()


@register.inclusion_tag('gallery/tags/recent_galleries_block.html')
def render_recent_galleries_block(limit=10):
    """ Renders last galleries block for index page.
    """
    qs = Gallery.objects.all().order_by('-id')[:limit]
    galleries_chunks = ichunks(2, qs)
    return locals()
