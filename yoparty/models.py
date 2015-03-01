from django.db import models as m
import random


RANDOM_ALLOWED_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
def random_string():
    return ''.join(random.choice(RANDOM_ALLOWED_CHARS) for _ in range(36))


class YoGroup(m.Model):
    """a Yo Group. cb_code es callback_code"""
    name = m.CharField(max_length=55)
    api_token = m.SlugField(max_length=36)
    passcode = m.SlugField(max_length=36, default=random_string)
    cb_code = m.SlugField(max_length=36, default=random_string)
    location_time = m.DateTimeField(null=True, blank=True)
    location_type = m.SlugField(max_length=1, choices=(
        ('M', 'Mean'),
        ('L', 'Location of first user'),
        ('U', 'User closer to the mean'),
    ), default='M')


    def __str__(self):
        return self.name


class YoMember(m.Model):
    group = m.ForeignKey(YoGroup, related_name='members')
    username = m.CharField(max_length=55)
    show_help = m.BooleanField(default=True)
    lat = m.FloatField(null=True, blank=True)
    lng = m.FloatField(null=True, blank=True)
    location_time = m.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username + ' of ' + self.group.__str__()

from django.contrib import admin
admin.site.register(YoGroup)
admin.site.register(YoMember)
