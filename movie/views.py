from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.views.generic.list import ListView
from .forms import MovieForm
from movie.models import Movies

# Create your views here.

class MovieList(ListView):
    model = Movies
    template_name = 'movie/single_user.html'
    context_object_name = 'movie_by_user'

    
    def get_queryset(self):
        return Movies.objects.filter(username=self.kwargs['pk'])



def loginuser(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('userdata')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('username doesnot exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("userdata")
        else:
            print("user doesnot exist")

    return render(request, 'movie/login_form.html')


def logoutuser(request):
    logout(request)
    return redirect('login')


def registeruser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('userdata')

    context = {
        'page': page,
        'form' : form
    }
    return render(request, 'movie/login_form.html', context)


def index(request):
    return render(request, 'movie/index.html')


@login_required(login_url='login')
def userdata(request):
    data = Movies.objects.all()
    context = {
        'data': data
    }
    return render(request, 'movie/ticket_info.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteticket(request, pk):
    ticket = Movies.objects.get(id=pk)
    if request.method == 'POST':
        ticket.delete()
        return redirect('userdata')
    context = {
        'object': ticket
    }
    return render(request, 'movie/delete_ticket.html', context)

