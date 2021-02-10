from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import ApiSerializer
from api.models import Api

class ApiView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Api.objects.all()
        serializer = ApiSerializer(qs, many=True)
        return Response(serializer.data)