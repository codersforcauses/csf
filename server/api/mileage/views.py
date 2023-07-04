from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mileage
from .serializers import MileageSerialiser


@api_view(['GET'])
def get_mileage(request, user_id):
  pass

@api_view(['POST'])
def post_mileage(request):
  pass