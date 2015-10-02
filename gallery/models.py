# coding: utf-8
from django.db import models
from django.conf import settings
from django.utils.functional import cached_property
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from pyuploadcare.dj import FileField, ImageField, ImageGroupField
from gallery.validators import extension_validator, size_validator


class AbstractGallery(models.Model):
    """ Abstract model for Gallery with common fields.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=300, blank=True)

    class Meta:
        abstract = True

    @property
    def cover(self):
        raise NotImplementedError

    @property
    def photo_items(self):
        raise NotImplementedError


@python_2_unicode_compatible
class Gallery(AbstractGallery):
    """ Simple gallery item.
    """
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:detail', args=(self.pk,))

    @cached_property
    def cover(self):
        return self.photo_set.first().image

    @cached_property
    def photo_items(self):
        return [{'url': p.image.cdn_url, 'title': p.title}
                for p in self.photo_set.all()]


@python_2_unicode_compatible
class GalleryMultiupload(AbstractGallery):
    """ Gallery with multiupload.
    """
    photos = ImageGroupField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:m_detail', args=(self.pk,))

    @cached_property
    def cover(self):
        return self.photos[0]

    @cached_property
    def photo_items(self):
        return [{'url': p.cdn_url, 'title': None} for p in self.photos]


@python_2_unicode_compatible
class Photo(models.Model):
    """ Simple photo item
    """
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=255)
    image = ImageField(validators=[size_validator, extension_validator])

    def __str__(self):
        return self.title
