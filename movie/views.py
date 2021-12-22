from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import MovieForm


from movie.models import Movies

# Create your views here.

def index(request):
    return render(request, 'movie/index.html')

def userdata(request):
    data = Movies.objects.all()
    context= {
        'data' : data
    }
    return render(request, 'movie/ticket_info.html',context)

def bookticket(request):
    form = MovieForm()
    context = {
        'form' : form

    }
    return render(request, 'movie/ticket-form.html',context)