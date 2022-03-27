from os import access
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse
import base64
from backend.settings import SOCIAL_AUTH_SPOTIFY_KEY, SOCIAL_AUTH_SPOTIFY_SECRET, LOGIN_REDIRECT_URL, SOCIAL_AUTH_SPOTIFY_SCOPE
import requests
import json

def index(request):
    return render(request, 'main.html')
    
def auth(request):
    url = 'https://accounts.spotify.com/authorize?'
    redirect_uri = 'http://127.0.0.1:8000/auth/complete/spotify/'

    params = {
        'client_id' : SOCIAL_AUTH_SPOTIFY_KEY,
        'response_type' : 'code', 
        'redirect_uri' : redirect_uri,
        'scope' : 'user-read-currently-playing'

    }
    code_req = requests.get(url, params)

    idk_dic = json.loads(code_req.content.strip()).json()
    # idk_dic = json.load(code_req.content)

    auth_code = idk_dic['code']

    return render(request, 'auth.html', idk_dic)


    # idk_dic = code_req.json()
    # idk_dic = {}
    
    # idk_dic = {"code": auth_code}
    # return render(request, 'auth.html', {'code':auth_code})

    # auth_code = request.GET.get('code', '')