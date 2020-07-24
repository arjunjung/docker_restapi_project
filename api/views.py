from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import ToyModel
from .toyserializers import ToySerializer
from rest_framework.response import Response
from rest_framework import status


class HomeTemplateView(TemplateView):
    template_name = 'api/home.html'


""" Flow of serializer
    Model Instance to Dict OR 
    Dict to Model Instace
"""

""" Flow of @api_view()
   - Limits the http verbs
   - Do automatic parsing of request data based on HTTP verb and Content Type.
   - Do choose render for particuar content type using ContentNegotiator class
   - Response returning rendered data based on content type too.
"""


@csrf_exempt
@api_view(['GET', 'POST'])
def toy_list(request):
    if request.method == 'GET':
        toy_all = ToyModel.objects.all()
        toy_serialized = ToySerializer(toy_all, many=True)
        return Response(toy_serialized.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        new_data_serialized = ToySerializer(data=request.data)
        if new_data_serialized.is_valid():
            new_data_serialized.save()
            return Response(new_data_serialized.data, status=status.HTTP_200_OK)
        return Response(new_data_serialized.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def toy_funs(request, pk):
    try:
        single_toy = ToyModel.objects.get(pk=pk)
    except ToyModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        single_toy_serialized = ToySerializer(single_toy)
        return Response(single_toy_serialized.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        new_updated_data = ToySerializer(request.data)
        if new_updated_data.is_valid():
            new_updated_data.save()
            return Response(new_updated_data.data, status=status.HTTP_200_OK)
        return Response(new_updated_data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        single_toy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
