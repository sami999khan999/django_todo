from rest_framework import serializers
from ..models import Todo, Projects, SubProjects
from .label_serializer import LabelsSerializer
from .projects_serializer import ProjectSerializer


class TodoSerializer(serializers.ModelSerializer):
    labels = LabelsSerializer(many=True, read_only=True)
    project = ProjectSerializer(source="project_id", read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = ["user_id"]
        extra_kwargs = {
            "project_id": {"write_only": True},
            "sub_project_id": {"write_only": True},
        }

    def create(self, validated_data):
        user = self.context.get("user")

        validated_data["user_id"] = user

        todo = Todo.objects.create(**validated_data)

        return todo
