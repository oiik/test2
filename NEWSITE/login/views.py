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
from django.contrib.auth.models import Group


def login(request):
    if request.user.is_authenticated:
        if request.user.groups.exists():
            return redirect('dl')
        else:
            return redirect('groups')
        # return redirect('dl')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password = password)

            if user is not None:
                djanjologin(request, user)
                if request.user.groups.exists():
                    return redirect('dl')
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
        return redirect('dl')
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


#Добавить доступ только для безгруппных
@login_required(login_url='login')
def groups(request):
    if request.method == 'POST':
        groupname = request.POST.get('groupname')
        # group = Group.objects.get(name='groupname')
        mgroup = Group.objects.get(name=groupname)
        mgroup.user_set.add(request.user)
        # request.user.groups.add(group)
        return redirect("dl")
    return render(request, 'login/groups.html')


@login_required(login_url='login')
def create_gp(request):
    if request.method == 'POST':
        groupname = request.POST.get('groupname')
        groupname, created = Group.objects.get_or_create(name=groupname)

        groupname = Group.objects.get(name=groupname)
        groupname.user_set.add(request.user)
        return redirect("dl")
    return render(request, 'login/create_gp.html')


@login_required(login_url='login')
def timetable(request):
    courses = Course.objects.all()
    return render(request, 'login/timetable.html', {'courses':courses})


@login_required(login_url='login')
def dl(request):
    if not request.user.groups.exists():
        return redirect('groups')
    else:
        gp = request.user.groups.all()[0]
        deads = Dead.objects.filter(group=gp).order_by('date')
    return render(request, 'login/dl.html', {'deads':deads})


@login_required(login_url='login')
def createDead(request):
    form = DeadForm()
    gp = request.user.groups.all()[0]
    if request.method == 'POST':
        form = DeadForm(request.POST)
        if form.is_valid():
            form.group = gp
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'login/createDead.html', context)


def deleteDead(request, id):
    Dead.objects.filter(id=id).delete()
    gp = request.user.groups.all()[0]
    deads = Dead.objects.filter(group=gp).order_by('date')
    return render(request, 'login/dl.html', {'deads':deads})
