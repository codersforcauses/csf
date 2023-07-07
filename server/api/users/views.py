from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User


@api_view(['PUT'])
def change_password(request):
    user = request.user
    if user.is_authenticated:
        print(request.data)
        if request.data["password"] == request.data["password_confirmation"]: 
            user.set_password(request.data["password"])
            return Response("Success")
        else:
            return Response("Passwords did not match", 400)
    else:
        return Response("Not logged in", 403)
