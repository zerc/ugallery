# coding: utf-8
from django.conf.urls import url

from . import views

urlpatterns = (
    url(r'^add/$', views.GalleryCreateView.as_view(), name='add'),

    url(r'^multi/add/$', views.GalleryMultiuploadCreateView.as_view(),
        name='multi_add'),

    url(r'^list/$', views.GalleryListView.as_view(), name='list'),

    url(r'^(?P<pk>\d+)/$', views.GalleryDetailView.as_view(), name='detail'),

    url(r'^m/(?P<pk>\d+)/$', views.GalleryMultiuploadDetailView.as_view(),
        name='m_detail'),

    url(r'^(?P<gallery_pk>\d+)/photos/add/$', views.PhotoCreateView.as_view(),
        name='photo_add'),
)
