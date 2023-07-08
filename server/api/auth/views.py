from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.auth.serializers import SignUpmodelSerializer


@api_view(['POST'])
def register(request):
    serializer = SignUpmodelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.create(request.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response((serializer.data, serializer.errors), status=status.HTTP_400_BAD_REQUEST)
