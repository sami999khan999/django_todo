from django.urls import path
from .views import user_views, todo_views, project_views, label_views, subproject_views

urlpatterns = [
    path("user/all/", user_views.get_all_user, name="get_all_users"),
    path("user/create/", user_views.create_user, name="create_user"),
    path(
        "todo/<uuid:pk>/",
        todo_views.get_todo_by_user,
        name="get_all_todo_from_user",
    ),
    path("todo/create/<uuid:pk>/", todo_views.create_todo, name="create_todo"),
    path(
        "todo/project/create/<uuid:pk>/",
        project_views.create_project,
        name="create_project",
    ),
    path("todo/label/create/<uuid:pk>/", label_views.create_label, name="create_label"),
    path(
        "todo/subproject/create/<uuid:pk>/",
        subproject_views.create_subproject,
        name="create_subproject",
    ),
]
