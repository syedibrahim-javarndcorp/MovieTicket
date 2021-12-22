from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm


from movie.models import Movies

# Create your views here.


def index(request):
    return render(request, 'movie/index.html')


def userdata(request):
    data = Movies.objects.all()
    context = {
        'data': data
    }
    return render(request, 'movie/ticket_info.html', context)


def bookticket(request):
    form = MovieForm()

    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userdata')

    context = {
        'form': form

    }
    return render(request, 'movie/ticket-form.html', context)


def changeticket(request, pk):
    change = Movies.objects.get(id=pk)
    form = MovieForm(instance=change)

    if request.method == "POST":
        form = MovieForm(request.POST, instance=change)
        if form.is_valid():
            form.save()
            return redirect('userdata')
    context = {
        'form': form

    }
    return render(request, 'movie/ticket-form.html', context)

def deleteticket(request,pk):
    ticket = Movies.objects.get(id=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('userdata')
    context = {
        'object' : ticket
    }
    return render(request,'movie/delete_ticket.html',context)