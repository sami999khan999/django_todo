from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..models import SubProjects, User
from ..serializers import SubprojectSerializer


@api_view(["POST"])
def create_subproject(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"message": "User doesn't exists"}, status=404)

    serializer = SubprojectSerializer(data=request.data, context={"user": user})

    if serializer.is_valid():
        subproject = serializer.save()

        return Response(SubprojectSerializer(subproject).data, status=200)

    return Response(serializer.errors, status=400)
