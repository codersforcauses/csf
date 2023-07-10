from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerialiser


@api_view(['GET'])
def get_user(request, username):
    user = User.objects.get(username=username)
    serializer = UserSerialiser(user)
    return Response(serializer.data)


