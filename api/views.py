from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer
from .models import User

@api_view(['GET'])
def get_users(request):
    # Get all users from database and serialize them
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)  # Return actual users from database

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)