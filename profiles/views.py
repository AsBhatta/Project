from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import user_profile
from .serializers import profileserializer


class profilelist(APIView):
    def get(self, request):
        profile= user_profile.objects.all()
        serializer = profileserializer(profile, many=True)
        return Response(serializer.data)

    def post(self):
        pass