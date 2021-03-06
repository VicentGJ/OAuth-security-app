from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, resolve_url
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from gsa import settings

def index(request):

    if request.user.is_authenticated:

        client_ip = request.META['REMOTE_ADDR']
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            client_ip = request.META['HTTP_X_FORWARDED_FOR']

        try:
            auth_user = Profile.objects.get(user__username=request.user)
            auth_user.last_IP = client_ip
            last_ip = auth_user.IPs.find(client_ip)
            if last_ip == -1:
                auth_user.IPs = auth_user.IPs + "," + client_ip
            auth_user.save()
        except:
            user = User.objects.get(username=request.user)
            auth_user = Profile(user=user, last_IP=client_ip, IPs=client_ip)
            auth_user.save()

        context = {
            'ip' : client_ip
        }
        
    else:
        context = {}

    return render(request, 'oauth/index.html', context)

def logout(request):
    login_url = resolve_url(settings.LOGIN_URL)
    return LogoutView.as_view(next_page=login_url)(request)

