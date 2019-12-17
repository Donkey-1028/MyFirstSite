from django.conf.urls import url
from .views import *

app_name = 'photo'

urlpatterns = [
    # /photo/
    url(r'^$', AlbumLV.as_view(), name='index'),
    # /photo/album/ same as /photo/
    url(r'^album/$', AlbumLV.as_view(), name='album_list'),
    # /photo/album/pk/
    url(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),
    # /photo/photo/pk/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),

    # /photo/album/add/
    url(r'^album/add/$', AlbumPhotoCV.as_view(), name='album_add'),
    # /photo/album/change/
    url(r'^album/add/change/$', AlbumChangeLV.as_view(), name='album_change'),
    # /photo/album/pk/update/
    url(r'^album/(?P<pk>[0-9]+)/update/$', AlbumPhotoUV.as_view(), name='album_update'),
    # /photo/album/pk/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$', AlbumDeleteView.as_view(), name='album_delete'),
    # /photo/photo/add/
    url(r'^photo/add/$', PhotoCreateView.as_view(), name='photo_add'),
    # /photo/photo/change/
    url(r'^photo/change/$', PhotoChangeLV.as_view(), name='photo_change'),
    # /photo/photo/pk/update/
    url(r'^photo/(?P<pk>[0-9]+)/update/$', PhotoUpdateView.as_view(), name='photo_update'),
    # /photo/photo/pk/delete/
    url(r'^photo/(?P<pk>[0-9]+)/delete/$', PhotoDeleteView.as_view(), name='photo_delete'),

]