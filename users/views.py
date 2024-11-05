# users/views.py
from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token

@extend_schema(
    tags=['users'],
    request=UserSerializer,
    responses={201: UserSerializer},
    description="Register a new user with full name, username, email, and password. The user role defaults to 'free'. Returns the user data and authentication token."
)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    tags=['users'],
    description="Login a user with email and password. Returns an authentication token if credentials are valid.",
    examples=[
        OpenApiExample(
            'Valid Login',
            summary="Example of valid login request",
            description="Request body for a successful login",
            value={
                "email": "user@example.com",
                "password": "password123"
            },
        )
    ],
    request={
        "application/json": {
            "email": "string",
            "password": "string"
        }
    },
    responses={
        200: OpenApiExample(
            'Login Response',
            summary="Successful login response",
            description="Returns the authentication token for the user",
            value={
                "token": "abcdef1234567890"
            }
        ),
        400: OpenApiExample(
            'Invalid Credentials',
            summary="Invalid login response",
            description="Error response when credentials are invalid",
            value={
                "error": "Invalid credentials"
            }
        )
    }
)
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(username=email, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)