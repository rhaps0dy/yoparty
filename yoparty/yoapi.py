from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

import requests
import re

from yoparty.models import YoGroup


GROUP_REGEX = r'^[A-Z0-9]+$'


def send_yo(username, api_token=None, link=None, location=None):
    """Send a yo"""
    query = {'api_token': api_token or settings.YOPARTY_API_TOKEN,
             'username': username}
    if link is not None:
        query['link'] = link
    if location is not None:
        query['location'] = location
    requests.post("http://api.justyo.co/yo/", data=query).json()


def exists(username):
    a = requests.get('https://api.justyo.co/check_username/',
                     data={'api_token': settings.YOPARTY_API_TOKEN,
                           'username': username})
    return a.json()['exists']


class GroupCreationError(Exception):
    pass


_group_regex_compiled = re.compile(GROUP_REGEX)
def create_group(group_name):
    """Creates a group. Raises GroupCreationError if the creation was not successful."""
    if not _group_regex_compiled.match(group_name):
        raise GroupCreationError("Group name must be all caps and only letters or numbers.")
    g = YoGroup(name=group_name)
    query = {'new_account_username': g.name,
             'new_account_passcode': g.passcode,
             'api_token': settings.YOPARTY_API_TOKEN,
             'needs_location': True,
             'description': "Yo, %s" % g.name,
             'callback': settings.BASE_URL + reverse('group_callback', kwargs={'cb_code': g.cb_code})}
    # Returns true if there is not an error, false if there was an error
    resp = requests.post('https://api.justyo.co/accounts/', data=query).json()
    if 'error' in resp:
        if resp['error'] == 'User already exists.':
            raise GroupCreationError("Yo user already exists.")
        raise GroupCreationError(resp['error'])
    g.api_token = resp['api_token']
    g.save()


def yo_all_in_group(group):
    requests.post("https://api.justyo.co/yoall/", data={"api_token": group.api_token})