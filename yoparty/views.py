from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.conf import settings
import requests


def send_yo(username, api_token=None, link=None, location=None):
    """Send a yo"""
    query = {'api_token': api_token or settings.YOPARTY_API_TOKEN,
             'username': username}
    if link is not None:
        query['link'] = link
    if location is not None:
        query['location'] = location
    requests.post("http://api.justyo.co/yo/", data=query)



def create_or_join_group(request):
    """Website to create a yoparty group"""
    # Possible opcio de enviar un yo a usuaris perque s'agreguin
    if request.method == "POST":
        return render(request, "yoparty/create_or_join_group.html", {"created": True})
    return render(request, "yoparty/create_or_join_group.html")


def yo_register(request):
    """Yo callback url that sends the link to the landing page"""
    if request.method != "GET" or "username" not in request.GET:
        raise PermissionDenied
    send_yo(request.GET['username'], link="http://www.upf.edu/")
    return HttpResponse("OK")


def yo_group(request, group):
    """Callback url for yo sent to any group. This receives yo's and locations, and sends back yo's and locations."""
    return HttpResponse(group)
