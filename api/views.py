from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import MovieSerializer
from movie.models import Movies



@api_view(['GET'])
def getroutes(request):

    routes = [
        {'GET': '/api/movie'},
    ]
    return Response(routes)


@api_view(['GET'])
def getmovies(request):
    movie = Movies.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getmovie(request, pk):
    movie = Movies.objects.get(id=pk)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def getsinglemovie(request, pk):
    movie = Movies.objects.get(id=pk)
    data = request.data

    movie, created = Movies.objects.get_or_create(
        title=movie,
    )
    movie.value = data['title']
    movie.save()
    serializer = MovieSerializer(movie, many=False)
    
    return Response(serializer.data)