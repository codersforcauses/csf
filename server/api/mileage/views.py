from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mileage
from .serializers import MileageSerialiser


@api_view(['GET'])
def get_mileage(request, user_id):
    event = Mileage.objects.get(user_id=user_id)
    serializer = MileageSerialiser(event)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def post_mileage(request):
    serialiser = MileageSerialiser(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
        return Response(serialiser.data)