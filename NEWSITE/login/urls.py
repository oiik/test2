from django.urls import path
from . import views
from django.views.generic import ListView,DetailView


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.dl, name="dl"),
    path('groups/', views.groups, name = 'groups'),
    path('create_gp/', views.create_gp, name = 'create_gp'),
    path('createDead/', views.createDead, name = 'createDead'),
    path('deleteDead/<int:id>/', views.deleteDead, name='deleteDead'),
]
