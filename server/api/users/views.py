from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.users.serializers import SignUpmodelSerializer

@api_view(['POST',])
def register(request):

    serializer = SignUpmodelSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
    else:
        data = serializer.errors
    return Response(data)

# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         data = request.body
#         firstname = data.get('firstname')
#         lastname = data.get('lastname')
#         password = data.get('password')
#         email = data.get('email')
#         print(firstname, lastname, password, email)
#         return Response('User registered successfully')
#     else:
#         return Response({'error': 'Method Not Allowed'}, status=405)