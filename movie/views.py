from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main.html')

def userdata(request,pk):
    return render(request, )
