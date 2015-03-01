from django.conf.urls import patterns, include, url
from yoparty import views
from yoparty.models import RANDOM_ALLOWED_CHARS
from yoparty.yoapi import GROUP_REGEX

urlpatterns = patterns('',
    url(r'^$', views.create_or_join_group),
    url(r'^help/(?P<group>' + GROUP_REGEX.strip("^$") + r')/(?P<username>' + GROUP_REGEX.strip("^$") + r')/$',
        views.help_page, name='help_page'),
    url(r'^cb/$', views.yo_register),
    url(r'^cb/(?P<cb_code>[' + RANDOM_ALLOWED_CHARS + r']+)/$', views.yo_group, name='group_callback'),
)
