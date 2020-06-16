from django.urls import path
from . import views
from django.views.generic import ListView,DetailView
from login.models import deadlines

urlpatterns = [
    #path('', views.home, name = 'home'), #создать home страничку
    #path('home/', views.home, name ='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.dl, name="dl"),
    path('groups/', views.groups, name = 'groups'),
    path('create_gp/', views.create_gp, name = 'create_gp'),
    path('deadlines/',ListView.as_view(queryset = deadlines.objects.all().order_by('deadlines'),
    template_name="/login/deadlines.html"), name = "deadlines"),
    path('deadlines/add', views.adddeadlines, name = 'adddeadlines'),
    # path('dl/', views.dl, name = 'dl'),
    path('createDead/', views.createDead, name = 'createDead'),
    path('deleteDead/<int:id>/', views.deleteDead, name='deleteDead'),


]
