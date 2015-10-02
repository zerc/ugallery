# coding: utf-8
from django import forms
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView
from django.utils.functional import cached_property

from . import models


class GalleryCreateView(CreateView):
    model = models.Gallery
    fields = ('title', 'user')

    def get_form_class(self):
        form_cls = super(GalleryCreateView, self).get_form_class()
        form_cls.base_fields['user'].widget = forms.HiddenInput()
        form_cls.base_fields['user'].initial = self.request.user
        return form_cls


class GalleryMultiuploadCreateView(GalleryCreateView):
    model = models.GalleryMultiupload
    fields = ('title', 'user', 'photos')
    template_name = 'gallery/gallery_form.html'


class PhotoCreateView(CreateView):
    model = models.Photo
    fields = ('title', 'image', 'gallery')

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


class GalleryDetailView(DetailView):
    model = models.Gallery


class GalleryMultiuploadDetailView(DetailView):
    model = models.GalleryMultiupload


class GalleryListView(ListView):
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
