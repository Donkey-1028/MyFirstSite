from django.conf.urls import url
from .views import *

app_name = 'blog'

urlpatterns = [
    # /blog/
    url(r'^$', PostLV.as_view(), name='index'),
    # /blog/post/ (same as /blog/)
    url(r'^post/$', PostLV.as_view(), name='post_list'),
    # /blog/post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
    # /blog/archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
    # /blog/2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
    # /blog/2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
    # /blog/2012/nov/18
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
    # /blog/today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
    # /blog/tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),
    # /blog/tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
    # /blog/search/
    url(r'^search/$', SearchFormView.as_view(), name='search'),

    # /blog/add/
    url(r'^add/$', PostCreateView.as_view(), name='add'),
    # /blog/change
    url(r'^change/$', PostChangeLV.as_view(), name='change'),
    # /blog/pk/update
    url(r'^(?P<pk>[0-9]+)/update/$', PostUpdateView.as_view(), name='update'),
    # /blog/pk/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', PostDeleteView.as_view(), name='delete'),



]