from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from django.contrib.auth.password_validation import validate_password
from .serializers import ChangePasswordSerializer, RequestResetPasswordSerializer, ResetPasswordSerializer
from django.core.exceptions import ValidationError

@api_view(['PATCH'])
def change_password(request):
    print(request.user)
    serializer = ChangePasswordSerializer(request.data)
    serializer.is_valid(raise_exception=True)
    
    # try: user = User.objects.get(username=request.data["username"]) 
    # except: return Response("Not logged in", 403)

    try:
        validate_password(serializer.data.password)
        request.user.set_password(serializer.data.password)
        request.user.save()
        return Response("Success")
    except ValidationError as e:
        return Response(list(e)[0])

@api_view(['POST'])
def request_reset_password(request):
    # try: user = User.objects.get(email=request.data["email"])
    # except: Response(status=404)
    # user.update(reset_token=uuid.uuid())

    print(request.user)

    serializer = RequestResetPasswordSerializer(request.data)
    serializer.is_valid(raise_exception=True)


    return Response("OK")


# resetToken
# newPassword