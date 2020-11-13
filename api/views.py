from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PeopleSerializer
from .models import People

# Create your views here.
@api_view(['GET'])
def PeopleList(request):
    people = People.objects.all()
    serializer = PeopleSerializer(people, many=True)
    return Response(serializer.data)