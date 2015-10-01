# coding: utf-8
from django import template
from django.conf import settings

from gallery import models

register = template.Library()


@register.inclusion_tag('gallery/render_gallery.html', takes_context=True)
def render_galleries(context, user):
    """ Renders galleries owned by user.
    """
    galleries = models.Gallery.objects.filter(user=user)
    galleries_multiupload = models.GalleryMultiupload.objects.filter(user=user)
    return locals()
