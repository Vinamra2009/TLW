from django.shortcuts import render
#Install the api view and the response object from rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
class HelloApiView(APIView):
    #Demo to accept get request
    #So whenever a get request is made to this APIview it will check for the get function in views

    def get(self, request, format=None):
        an_apiview = [
            'USES HTTP methods',
            'Similar to Django view',
            'Gives most control',
        ]

        return Response({'message':'Hello','an_apiview': an_apiview})