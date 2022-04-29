from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('users/', views.users, name='users'),
    path('users/<int:user_id>/', views.get_user),
    path('users/new/', views.save_user),
]