from rest_framework import serializers
from ..models import SubProjects


class SubprojectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProjects
        fields = "__all__"
        read_only_fields = ["user_id"]

    def create(self, validated_data):
        user = self.context.get("user")

        validated_data["user_id"] = user

        subproject = SubProjects.objects.create(**validated_data)

        return subproject
