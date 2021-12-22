from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MovieSerializer
from movie.models import Movies

from api import serializer

@api_view(['GET'])
def getroutes(request):

    routes = [
        {'GET' : '/api/movie'},
    ]
    return Response(routes)


@api_view(['GET'])
def getmovie(request):
    movie = Movies.objects.all()
    serializer = MovieSerializer(movie, many=True)
    return Response(serializer.data)