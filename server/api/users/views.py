from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import RequestResetPasswordSerializer

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

@api_view(['POST'])
def request_reset_password(request):
    # try: user = User.objects.get(email=request.data["email"])
    # except: Response(status=404)
    # user.update(reset_token=uuid.uuid())

    serializer = RequestResetPasswordSerializer(request.data)
    if not serializer.is_valid(): return Response(status=404)


    return Response("OK")