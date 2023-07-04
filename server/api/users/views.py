# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        data = request.body
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        password = data.get('password')
        email = data.get('email')
        print(firstname, lastname, password, email)
        return Response('User registered successfully')
    else:
        return Response({'error': 'Method Not Allowed'}, status=405)