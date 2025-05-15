from django.db import models
import uuid
from django.utils import timezone


# need to cache to improve performance
admin_email_env = "sami999khan999@gmail.com"


# user model
class User(models.Model):
    class RoleChoices(models.TextChoices):
        ADMIN = "Admin"
        USER = "User"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(
        max_length=10, choices=RoleChoices.choices, default=RoleChoices.USER
    )

    def __str__(self):
        return self.name

    @classmethod
    def create_user_with_role(cls, **kwargs):
        admin_email = admin_email_env

        user_data = kwargs.copy()

        if user_data.get("email") == admin_email:
            user_data["role"] = cls.RoleChoices.ADMIN

        return cls.objects.create(**user_data)


# =====================================================#
# project model


class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)


# =====================================================#
# sub-project model


class SubProjects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


# =====================================================#
# todo model

from django.db import models
import uuid


class Labels(models.Model):
    class ColorChoices(models.TextChoices):
        BERRY_RED = "Berry Red", "Berry Red"
        RED = "Red", "Red"
        ORANGE = "Orange", "Orange"
        YELLOW = "Yellow", "Yellow"
        OLIVE_GREEN = "Olive Green", "Olive Green"
        LIME_GREEN = "Lime Green", "Lime Green"
        GREEN = "Green", "Green"
        MINT_GREEN = "Mint Green", "Mint Green"
        TEAL = "Teal", "Teal"
        SKY_BLUE = "Sky Blue", "Sky Blue"
        LIGHT_BLUE = "Light Blue", "Light Blue"
        BLUE = "Blue", "Blue"
        GRAPE = "Grape", "Grape"
        VIOLET = "Violet", "Violet"
        LAVENDER = "Lavender", "Lavender"
        MAGENTA = "Magenta", "Magenta"
        SALMON = "Salmon", "Salmon"
        CHARCOAL = "Charcoal", "Charcoal"
        GREY = "Grey", "Grey"
        TAUPE = "Taupe", "Taupe"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(
        max_length=20, choices=ColorChoices.choices, default=ColorChoices.GREY
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.color})"


# =====================================================#
# todo model


class Todo(models.Model):
    class PriorityChoices(models.Choices):
        HIGH = "high"
        MEDIUM = "medium"
        LOW = "low"
        NONE = "none"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(
        Projects, on_delete=models.CASCADE, null=True, blank=True
    )
    sub_project_id = models.ForeignKey(
        SubProjects, on_delete=models.CASCADE, null=True, blank=True
    )
    labels = models.ManyToManyField(Labels, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.TextField(
        max_length=10, choices=PriorityChoices.choices, default=PriorityChoices.NONE
    )
    due_date = models.DateTimeField(null=True, blank=True)
    reminder = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
