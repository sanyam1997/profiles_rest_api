from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView( APIView ) :
    """Test API View."""

    def get( self , request , format = None ) :
        """Return a list of API features."""
        an_apiview = [
            'Uses HTTP method as functions (get, post, patch, put, delete)' ,
            'Is similar to a traditional Django View' ,
            'Gives you most control over logic' ,
            'Is mapped manually to URLs'
        ]

        return Response( { 'message' : 'hello!' , 'an_apiview' : an_apiview } )
