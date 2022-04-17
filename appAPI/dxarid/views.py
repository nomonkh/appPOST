from celery import shared_task
from django.shortcuts import render
from django.forms import model_to_dict
from django.shortcuts import render

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from dxarid.models import Main, Products
from .tasks import post
# authentication_classes = [SessionAuthentication, BasicAuthentication]
# permission_classes = (IsAuthenticated,)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_post(request):
    if request.method == 'GET':
        lst = Main.objects.all().values()
        return Response({
                'data': 'empty' if len(list(lst)) == 0 else lst
        })
    elif request.method == 'POST':
        post(request.data)
        return Response({'message': [ids['lot_info']['id'] for ids in request.data]})
