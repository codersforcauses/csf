from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.users.serializers import SignUpmodelSerializer

@api_view(['POST'])
def register(request):

    serializer = SignUpmodelSerializer(data=request.data)
    print("data:", request.data)
    data = {}
    if serializer.is_valid():
        print('hi')
        account = serializer.save()
        print(account)
    else:
        print('hiasdf')
        data = serializer.errors
    return Response(data)
