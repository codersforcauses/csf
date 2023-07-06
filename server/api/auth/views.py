from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_fraemwork.response import Response

from .serializers import SignUpmodelSerializer

class registerUser(CreateAPIView):
    serializer_class = SignUpmodelSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)