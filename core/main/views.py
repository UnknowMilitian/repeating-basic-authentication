import base64
from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer, RegisterSerializer
from .authentication import CustomBasicAuthentication


# Create your views here.
class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CustomBasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Encode username and password in base64
        credentials = f"{user.username}:{request.data['password']}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        # Print encoded credentials to the terminal
        print(f"Base64 Encoded Credentials on Registration: {encoded_credentials}")

        return Response(
            {
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
                "message": "User is registered successfully!",
            },
            status=status.HTTP_201_CREATED,
        )
