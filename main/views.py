from changemaker.models import ChangeMaker
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.core.mail import send_mail

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .decorators import *


def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']

        subject = 'Query from ' + name
        message = 'Hi Social Vision, ' + query
        # send an email

        send_mail(subject, message, email, ['contact.socialvision@gmail.com'])

        context = {
            'name': name,
        }
    else:
        context = {}

    return render(request, 'main/home.html', context)


def about(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']

        subject = 'Query from ' + name
        message = 'Hi Social Vision, ' + query
        # send an email

        send_mail(subject, message, email, ['contact.socialvision@gmail.com'])

        context = {
            'name': name,
        }
    else:
        context = {}

    return render(request, 'main/about.html')


def covid(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']

        subject = 'Query from ' + name
        message = 'Hi Social Vision, ' + query
        # send an email

        send_mail(subject, message, email, ['contact.socialvision@gmail.com'])

        context = {
            'name': name,
        }
    else:
        context = {}

    return render(request, 'main/covid.html')


def donate(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']

        subject = 'Query from ' + name
        message = 'Hi Social Vision, ' + query
        # send an email

        send_mail(subject, message, email, ['contact.socialvision@gmail.com'])

        context = {
            'name': name,
        }
    else:
        context = {}

    return render(request, 'main/donate.html', context)


@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'main/login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


@unauthenticated_user
def registerUser(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

    context = {
        'form': form,
    }

    return render(request, 'main/register.html', context)


def profileUser(request):
    user = request.user

    groups = None
    if request.user.groups.exists():
        groups = set(group.name for group in request.user.groups.all())
        for group in groups:
            if group == "changemaker":
                isChangeMaker = True
                break
            else:
                isChangeMaker = False

        for group in groups:
            if group == "trainee":
                isTrainee = True
                break
            else:
                isTrainee = False


    context = {
        'user': user,
        'isChangeMaker' : isChangeMaker,
        'isTrainee' : isTrainee,
    }

    return render(request, 'main/profile.html', context)
