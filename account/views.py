from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, UserDataSerializer


# Create your views here.

class RegistrationAPIView(APIView):
    @swagger_auto_schema(
        request_body=RegisterSerializer,
        operation_description="Get a single post",
        operation_summary="Get post",
        tags=["posts"],
    )
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            data['message'] = 'Your account has been created successfully'
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""This view handles JWT login. Subclasses it because I added a custom claim to the CustomTokenObtainPairSerializer and also changed it to use email for authentication"""
class LoginWithEmailView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


"""View to get user data"""
class GetUserDataAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        serializer = UserDataSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
