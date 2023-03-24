"""In Django REST Framework, APIView is a class-based view that provides a powerful
 and flexible way to build web APIs. It is a base class from which other classes
 can inherit and define methods for handling HTTP requests and generating HTTP responses.

The APIView class provides a set of default methods for handling different types
of HTTP requests, such as GET, POST, PUT, DELETE, and more. It also provides hooks
for performing custom authentication and permission checks, as well as
customizable response rendering.

One of the benefits of using APIView is that it allows you to define a single
endpoint that can handle multiple HTTP methods, rather than creating separate
views for each method. This can help simplify your code and reduce duplication.

"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
# Create your views here.

class HelloApiView(APIView):
    """test API View """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIviews features"""
        an_apiview = [
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you th emost control over you application logic',
        'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview })

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete AN OBJECT"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""
        a_viewset= [
            'Uses actions (list, create, retrive, update, partial_update)',
            'Automatically mapps to URLs using Routers',
            'Provides more functionally with less code',
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})

    def create(self,request ):
        """Create a new hello message"""
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message })
        else:
            return Reponse(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating a object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating a part of an object """
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})        
