from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import *
from .forms import CreateUserForm

def home(request):
    return render(request, 'login/home.html')

def login(request):
    return render(request, 'login/login.html')

def register(request):
    #form = UserCreationForm()
    form = CreateUserForm() # Форма с дополнениями(email) заменить
    # Она лежит в forms.py
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    conrext = {'form':form}
    return render(request, 'login/register.html')

def timetable(request):
    courses = Course.objects.all()
    return render(request, 'login/timetable.html', {'courses':courses})
