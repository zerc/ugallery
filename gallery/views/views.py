# coding: utf-8
from django import forms
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.utils.functional import cached_property

from gallery import models
from .base import AbstractCreateView, AbstractDetailView, AbstractUpdateView


__ALL__ = ('GalleryListView',
           'GalleryDetailView', 'GalleryMultiuploadDetailView',
           'GalleryCreateView', 'GalleryMultiuploadCreateView',
           'PhotoCreateView',
           'GalleryUpdateView', 'GalleryMultiuploadUpdateView')


class GalleryListView(ListView):
    """ List of all galleries owned by current user.
    """
    model = models.Gallery

    def get_queryset(self, *args, **kwargs):
        qs = super(GalleryListView, self).get_queryset(*args, **kwargs)
        return qs.filter(user=self.request.user).prefetch_related('photo_set')

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryListView, self).get_context_data(*args,
                                                                **kwargs)
        context['m_galleries'] = models.GalleryMultiupload.objects.filter(
            user=self.request.user)

        return context


# Detail views
class GalleryDetailView(AbstractDetailView):
    model = models.Gallery


class GalleryMultiuploadDetailView(AbstractDetailView):
    model = models.GalleryMultiupload
    show_add = False
    update_url = 'gallery:m_update'


# Create views
class GalleryCreateView(AbstractCreateView):
    model = models.Gallery


class GalleryMultiuploadCreateView(AbstractCreateView):
    model = models.GalleryMultiupload
    fields = AbstractCreateView.fields + ('photos',)


class PhotoCreateView(AbstractCreateView):
    model = models.Photo
    fields = ('title', 'image', 'gallery')

    form_title = 'Add a new photo'
    button_title = 'Add!'
    button_icon = 'camera'

    @cached_property
    def gallery(self):
        return get_object_or_404(models.Gallery,
                                 pk=self.kwargs.get('gallery_pk'))

    def get_form_class(self):
        form_cls = super(PhotoCreateView, self).get_form_class()
        form_cls.base_fields['gallery'].widget = forms.HiddenInput()
        form_cls.base_fields['gallery'].initial = self.gallery.pk
        return form_cls

    def get_success_url(self):
        return self.gallery.get_absolute_url()


# Update views
class GalleryUpdateView(AbstractUpdateView):
    model = models.Gallery


class GalleryMultiuploadUpdateView(AbstractUpdateView):
    model = models.GalleryMultiupload
    fields = AbstractCreateView.fields + ('photos',)
