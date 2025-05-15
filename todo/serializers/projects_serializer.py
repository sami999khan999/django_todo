from rest_framework import serializers
from ..models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"
        read_only_fields = ["user_id"]

    def create(self, validated_data):
        user = self.context.get("user")

        if user:
            validated_data["user_id"] = user

        project = Projects.objects.create(**validated_data)
        return project
