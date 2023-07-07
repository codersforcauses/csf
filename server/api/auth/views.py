from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
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



# class RegistrationView(CreateAPIView):
#     serializer_class = SignUpmodelSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         print(request.data)
#         if serializer.is_valid():
#             self.perform_create(serializer)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)