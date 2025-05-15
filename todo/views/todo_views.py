from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers import TodoSerializer
from ..models import User, Todo, Projects
from rest_framework import status


# get todo by user id
@api_view(["GET"])
def get_todo_by_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"message": "User Not found"}, status=404)

    todo = Todo.objects.filter(user=user)

    if not todo.exists:
        return Response({"message": "No todos found for this user"}, status=404)

    serializer = TodoSerializer(todo)

    return Response(serializer, status=200)


# create todo
@api_view(["POST"])
def create_todo(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(
            {"message": "User not found."}, status=status.HTTP_404_NOT_FOUND
        )

    serializer = TodoSerializer(data=request.data, context={"user": user})

    if serializer.is_valid():
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=201)
    return Response(serializer.errors, status=400)
