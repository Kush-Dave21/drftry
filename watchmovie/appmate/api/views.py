from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from appmate.api.serializers import *

# class MovieListAV(APIView):
    # def get(self, request):
    #     movies = Movie.objects.all()
    #     serializer = MovieSerializer(movies, many=True)
    #     return Response(serializer.data)

    # def post(self,request):
        # serializer = MovieSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)