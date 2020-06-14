from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as djanjologin
from django.contrib.auth.decorators import login_required



def login(request):
    if request.user.is_authenticated:
        # if request.user.groups.exists():
        #     return redirect('timetable')
        # else:
        #     return redirect('groups')
        return redirect('timetable')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)

            if user is not None:
                djanjologin(request, user)
                # return redirect('timetable')
                if request.user.groups.exists():
                    return redirect('timetable')
                else:
                    return redirect('groups')
            else:
                messages.info(request, 'Логин или пароль введен неверно')
        context = {}
        return render(request, 'login/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('timetable')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, user +' вы создали аккаунт.' )
                return redirect('login')
        context = {'form':form}
        return render(request, 'login/register.html', context)

@login_required(login_url='login')
def groups(request):
    return render(request, 'login/groups.html')

@login_required(login_url='login')
def create_gp():

    
    return render(request, 'login/create_gp')

@login_required(login_url='login')
def home(request):
    return render(request, 'login/home.html')


@login_required(login_url='login')
def timetable(request):
    courses = Course.objects.all()
    return render(request, 'login/timetable.html', {'courses':courses})

@login_required(login_url='login')
def adddeadlines(request):
    form2 = CreatedeadlinesForm(request.POST or None)
    if request.method == 'POST' and form2.is_valid():
        form2.save()
        return redirect('deadlines')
    return render(request, 'login/adddeadlines.html',{'form2':form2})
