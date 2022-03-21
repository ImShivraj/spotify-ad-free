from django.http import HttpRequest
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main.html')
    
def auth(request):
    return render(request, 'auth.html')

    
    
