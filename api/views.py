from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getroutes(request):

    routes = [
        {'GET' : '/api/movie'},
    ]
    return Response(routes)