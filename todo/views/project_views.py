from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..serializers import ProjectSerializer
from ..models import Projects, User


@api_view(["POST"])
def create_project(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"message": "User doesn't exists"}, status=404)

    serializer = ProjectSerializer(data=request.data, context={"user": user})

    if serializer.is_valid():
        project = serializer.save()

        project_data = ProjectSerializer(project).data

        return Response(project_data, status=200)
    return Response(serializer.errors, status=400)
