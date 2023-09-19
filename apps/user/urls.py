from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.users_list, name='user_list'),
    path('login/', views.login_view, name='login-view'),
    path('profile/', views.profile, name='profile'),
]