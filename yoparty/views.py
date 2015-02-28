from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.conf import settings
from yoparty import yoapi


def create_or_join_group(request):
    """Website to create a yoparty group"""
    # Possible opcio de enviar un yo a usuaris perque s'agreguin
    if request.method == "POST":
        if "group" not in request.POST or request.POST["group"] == "":
            return render
        try:
            yoapi.create_group(request.POST["group"])
        except yoapi.GroupCreationError as e:
            return render(request, "yoparty/create_or_join_group.html", {"error": str(e)})
        return render(request, "yoparty/create_or_join_group.html", {"created": True})
    return render(request, "yoparty/create_or_join_group.html")


def yo_register(request):
    """Yo callback url that sends the link to the landing page"""
    if request.method != "GET" or "username" not in request.GET:
        raise PermissionDenied
    yoapi.send_yo(request.GET['username'], link=settings.BASE_URL + "/")
    return HttpResponse("OK")


def yo_group(request, cb_code):
    """Callback url for yo sent to any group. This receives yo's and locations, and sends back yo's and locations."""

    return HttpResponse("OK")
