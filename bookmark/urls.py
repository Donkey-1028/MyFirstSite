from django.conf.urls import url
from .views import *


app_name = 'bookmark'

urlpatterns =[
    # /bookmark/
    url(r'^$', BookmarkLV.as_view(), name='index'),
    # /bookmark/숫자/
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),

    # /bookmark/add/
    url(r'^add/$', BookmarkCreateView.as_view(), name='add'),
    # /bookmark/change
    url(r'^change/$', BookmarkChangeLV.as_view(), name='change'),
    # /bookmark/pk/update
    url(r'^(?P<pk>[0-9]+)/update/$', BookmarkUpdateView.as_view(), name='update'),
    # /bookmark/pk/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', BookmarkDeleteView.as_view(), name='delete'),
]