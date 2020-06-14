from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'), #создать home страничку
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('timetable/', views.timetable, name="timetable"),
]
