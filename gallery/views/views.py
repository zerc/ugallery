# coding: utf-8
from django import forms
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import BaseDeleteView, TemplateResponseMixin
from django.utils.functional import cached_property

from gallery import models

from .base import AbstractCreateView, AbstractDetailView, AbstractUpdateView


__ALL__ = ('GalleryListView', 'GalleryDetailView', 'GalleryCreateView',
           'GalleryUpdateView', )


class GalleryListView(ListView):
    """ List of all galleries owned by current user.
    """
    model = models.Gallery

    def get_queryset(self, *args, **kwargs):
        qs = super(GalleryListView, self).get_queryset(*args, **kwargs)
        return qs.filter(user=self.request.user).prefetch_related('photo_set')


class GalleryDetailView(AbstractDetailView):
    model = models.Gallery


class GalleryCreateView(AbstractCreateView):
    model = models.Gallery


class GalleryUpdateView(AbstractUpdateView):
    model = models.Gallery


class PhotoDeleteView(TemplateResponseMixin, BaseDeleteView):
    model = models.Photo
    content_type = 'application/json'

    def get_queryset(self, *args, **kwargs):
        """ Only owner of gallery can delete the photo.
        """
        qs = super(PhotoDeleteView, self).get_queryset(*args, **kwargs)
        return qs.filter(gallery__user=self.request.user)

    def delete(self, request, *args, **kwargs):
        super(PhotoDeleteView, self).delete(request, *args, **kwargs)
        return JsonResponse({})

    def get_success_url(self):
        return None
