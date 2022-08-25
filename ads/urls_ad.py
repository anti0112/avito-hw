from ads.views import *
from django.urls import path

urlpatterns = [
    path("", AdListView.as_view(), name="home"),
    path("<int:pk>/", AdDetailView.as_view(), name="get_pk"),
    path("create/", AdCreateView.as_view(), name="create"),
    path("<int:pk>/update/", AdUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", AdDeleteView.as_view(), name="delete"),
    
] 
