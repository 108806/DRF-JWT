from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework import serializers
from users.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.
class UserDetailAPI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(user)

        return Response(serializer.data)
