from users.views import *
from django.urls import path

urlpatterns = [
    path("", UserListView.as_view(), name="home"),
    path("<int:pk>/", UserDetailView.as_view(), name="get_pk"),
    path("create/", UserCreateView.as_view(), name="create"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete"),
]