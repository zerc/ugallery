# coding: utf-8
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from pyuploadcare.dj import FileField, ImageField, ImageGroupField


class AbstractGallery(models.Model):
    """ Abstract model for Gallery with common fields.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Gallery(AbstractGallery):
    """ Simple gallery item.
    """
    def __str__(self):
        return self.title


@python_2_unicode_compatible
class GalleryMultiupload(AbstractGallery):
    """ Gallery with multiupload.
    """
    photos = ImageGroupField()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Photo(models.Model):
    """ Simple photo item
    """
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=255)
    image = ImageField()

    def __str__(self):
        return self.title
