# coding: utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^add/$',
        login_required(views.GalleryCreateView.as_view()),
        name='add'),

    url(r'^multi/add/$',
        login_required(views.GalleryMultiuploadCreateView.as_view()),
        name='multi_add'),

    url(r'^list/$', login_required(views.GalleryListView.as_view()),
        name='list'),

    url(r'^(?P<pk>\d+)/$',
        login_required(views.GalleryDetailView.as_view()),
        name='detail'),

    url(r'^(?P<pk>\d+)/update$',
        login_required(views.GalleryUpdateView.as_view()),
        name='update'),

    url(r'^m/(?P<pk>\d+)/$',
        login_required(views.GalleryMultiuploadDetailView.as_view()),
        name='m_detail'),

    url(r'^m/(?P<pk>\d+)/update$',
        login_required(views.GalleryMultiuploadUpdateView.as_view()),
        name='m_update'),

    url(r'^(?P<gallery_pk>\d+)/photos/add/$',
        login_required(views.PhotoCreateView.as_view()),
        name='photo_add'),
)
