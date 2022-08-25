from ads.views import *
from django.urls import path

urlpatterns = [
    path("", CategoryListView.as_view(), name="home"),
    path("<int:pk>/", CategoryDetailView.as_view(), name="get_pk"),
    path("create/", CategoryCreateView.as_view(), name="create"),
    path("<int:pk>/update/", CategoryUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete"),
    
]