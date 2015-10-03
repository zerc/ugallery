# coding: utf-8
from django.contrib import admin

from . import models


class PhotoInline(admin.StackedInline):
    model = models.Photo


@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
