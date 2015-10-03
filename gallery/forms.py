# coding: utf-8
from django import forms
from pyuploadcare.dj.forms import ImageGroupField
from pyuploadcare.api_resources import FileGroup

from gallery.models import Gallery, Photo


class GalleryForm(forms.ModelForm):
    photos = ImageGroupField(required=False)

    class Meta:
        model = Gallery
        fields = ('title', 'user', 'short_description')

    def save(self, *args, **kwargs):
        obj = super(GalleryForm, self).save(*args, **kwargs)

        photos = self.cleaned_data.get('photos', None)
        if photos:
            self.save_photos(obj, photos)

        return obj

    def save_photos(self, gallery, group_cdn_url):
        group = FileGroup(group_cdn_url)

        for i, f in enumerate(group):
            Photo(gallery=gallery, title='Photo #{}'.format(i+1),
                  image=f).save()
