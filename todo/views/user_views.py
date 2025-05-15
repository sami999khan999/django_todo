from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers import UserSerializer
from ..models import User
from rest_framework import status


@api_view(["GET"])
def get_all_user(request):
    users = User.objects.all()

    serializer = UserSerializer(users, many=True)

    return Response(serializer.data, status=200)


@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = User.create_user_with_role(**serializer.validated_data)

        user_data = UserSerializer(user).data

        return Response(
            {"user": user_data, "status": "success"},
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
