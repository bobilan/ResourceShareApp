from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.users_list, name='user_list')
]
