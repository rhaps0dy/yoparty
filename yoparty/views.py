from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from yoparty import yoapi
from yoparty.models import YoGroup, YoMember


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


#def join_success_page(request, group):
#    return render(request, "yoparty/message.html",
#                  {'title': "Join success!",
#                   "message": "You have joined group %s." % group})

def help_page(request, group, username):
    if request.METHOD == "POST":
        u = get_object_or_404(YoMember, group__name=group, username=username)
        u.show_help = False
        u.save(update_fields=['show_help'])
        return render(request, "yoparty/message.html",
                      {"title": "Help disabled.",
                       "message": "You will no longer receive the help page."})
    return render(request, "yoparty/help_page.html")


def yo_register(request):
    """Yo callback url that sends the link to the landing page"""
    if request.method != "GET" or "username" not in request.GET:
        raise Http404
    yoapi.send_yo(request.GET['username'], link=settings.BASE_URL + "/")
    return HttpResponse()


def yo_group(request, cb_code):
    """Callback url for yo sent to any group. This receives yo's and locations, and sends back yo's and locations."""
    if request.method != "GET" or "username" not in request.GET:
        raise Http404
    g = get_object_or_404(YoGroup, cb_code=cb_code)
    u, created = YoMember.objects.get_or_create(group=g, username=request.GET["username"])
    if created:
        u.save()
        yoapi.send_yo(u.username, api_token=g.api_token,
                      link=settings.BASE_URL + reverse('help_page',kwargs={'group': g.name, 'username': u.username}))
        return HttpResponse()
    if "location" in request.GET:
        print("location")
    yoapi.yo_all_in_group(g)
    return HttpResponse()
