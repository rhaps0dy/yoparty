from django.conf.urls import patterns, include, url
from yoparty import views

urlpatterns = patterns('',
    url(r'^$', views.create_or_join_group),
    url(r'^cb/$', views.yo_register),
    url(r'^cb/(?P<group>[A-Z0-9]+)/$', views.yo_group),
)
