from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mileage
from .serializers import MileageSerializer


@api_view(['GET'])
def get_mileage(request, user):
    if (request.user.is_authenticated is False):
        return Response("User not authenticated", status=401)
    else: 
        mileages = Mileage.objects.filter(user=user)
        serializer = MileageSerializer(mileages, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def post_mileage(request):
    if (request.user.is_authenticated is False):
        return Response("User not authenticated", status=401)
    else:
        serializer = MileageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
