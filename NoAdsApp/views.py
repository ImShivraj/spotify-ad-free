from os import access
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
import base64
from backend.settings import SOCIAL_AUTH_SPOTIFY_KEY, SOCIAL_AUTH_SPOTIFY_SECRET, LOGIN_REDIRECT_URL
import requests

def index(request):
    return render(request, 'main.html')
    
def auth(request):
    auth_code = request.GET.get('code', '')
    # idk_dic['code'] = auth_code
    # idk_dic = {"code": auth_code}
    # return render(request, 'auth.html', idk_dic)
    return render(request, 'auth.html', {'code':auth_code})
