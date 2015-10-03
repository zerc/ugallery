# coding: utf-8
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = (
    url(r'^add/$',
        login_required(views.GalleryCreateView.as_view()),
        name='add'),

    url(r'^list/$', views.GalleryListView.as_view(),
        name='list'),

    url(r'^(?P<pk>\d+)/$',
        views.GalleryDetailView.as_view(),
        name='detail'),

    url(r'^photo/(?P<pk>\d+)/$',
        login_required(views.PhotoDeleteView.as_view()),
        name='photo-delete'),

    url(r'^(?P<pk>\d+)/update$',
        login_required(views.GalleryUpdateView.as_view()),
        name='update'),
)
