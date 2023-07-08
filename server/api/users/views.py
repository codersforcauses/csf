from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from django.contrib.auth.password_validation import validate_password

@api_view(['PUT'])
def change_password(request):
    data = request.data
    # for some reason request.user doesn't work, it always returns an anonymous user
    # so instead pass the username in the request too
    try:
        user = User.objects.get(username=data["username"]) 
        if request.data["password"] == request.data["password_confirmation"]: 
            try:
                validate_password(request.data["password"])
                user.set_password(request.data["password"])
                user.save()
                return Response("Success")
            except:
                return Response("Invalid")
        else:
            return Response("Passwords did not match")
    except:
        return Response("Not logged in", 403)
