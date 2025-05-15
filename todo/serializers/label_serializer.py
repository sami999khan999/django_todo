from rest_framework import serializers
from ..models import Labels


class LabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = "__all__"
        read_only_fields = ["user_id"]

    def create(self, validated_data):
        user = self.context.get("user")

        print(validated_data)

        validated_data["user_id"] = user

        label = Labels.objects.create(**validated_data)

        return label
