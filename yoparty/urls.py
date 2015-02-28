from django.conf.urls import patterns, include, url
from yoparty import views
from yoparty.models import RANDOM_ALLOWED_CHARS

urlpatterns = patterns('',
    url(r'^$', views.create_or_join_group),
    url(r'^cb/$', views.yo_register),
    url(r'^cb/(?P<cb_code>[' + RANDOM_ALLOWED_CHARS + r']+)/$', views.yo_group, name='group_callback'),
)
