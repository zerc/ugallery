# coding: utf-8
from django import forms
from django.views.generic import CreateView, DetailView, UpdateView


class GalleryFormMixin(object):
    """ Mixin for forms of `gallery` module.
    """
    fields = ('title', 'short_description', 'user')
    template_name = 'gallery/gallery_form.html'

    form_title = 'Create a new gallery'
    button_title = 'Create!'
    button_icon = 'star'

    def get_form_class(self):
        form_cls = super(GalleryFormMixin, self).get_form_class()

        if 'user' in form_cls.base_fields:
            form_cls.base_fields['user'].widget = forms.HiddenInput()
            form_cls.base_fields['user'].initial = self.request.user

        return form_cls

    def get_context_data(self, *args, **kwargs):
        context = super(GalleryFormMixin,
                        self).get_context_data(*args, **kwargs)
        context.update(dict(
            form_title=self.form_title,
            button_title=self.button_title,
            button_icon=self.button_icon
        ))

        return context


class AbstractCreateView(GalleryFormMixin, CreateView):
    """ Common CreateView for galleries and photos.
    """


class AbstractUpdateView(GalleryFormMixin, UpdateView):
    """ Common UpdateView for galleries and photos.
    """
    form_title = 'Update a gallery'
    button_title = 'Update!'


class AbstractDetailView(DetailView):
    """ Abstract DetailView for single gallery item.
    """
    template_name = 'gallery/gallery_detail.html'
    show_add = True
    update_url = 'gallery:update'

    def get_queryset(self, *args, **kwargs):
        qs = super(AbstractDetailView, self).get_queryset(*args, **kwargs)
        return qs.filter(user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(AbstractDetailView, self).get_context_data(*args,
                                                                   **kwargs)
        context.update(dict(
            show_add=self.show_add,
            update_url=self.update_url
        ))

        return context
