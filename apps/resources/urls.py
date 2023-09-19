from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('resource/<int:id>', views.resource_detail, name="resource-details"),
    path('resource/post/', views.resource_post, name="resource-post"),
]