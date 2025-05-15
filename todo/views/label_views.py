from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from ..serializers import LabelsSerializer
from ..models import User


@api_view(["POST"])
def create_label(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=404)

    serializer = LabelsSerializer(data=request.data, context={"user": user})

    if serializer.is_valid():
        label = serializer.save()
        return Response(LabelsSerializer(label).data, status=200)

    return Response(serializer.error_messages, status=400)
