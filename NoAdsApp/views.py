from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main.html')
    # return HttpResponse("this is homepage")

def login(request):
    return HttpResponse("this is login page")