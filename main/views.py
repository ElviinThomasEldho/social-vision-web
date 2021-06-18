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

from trainee import views as trainee
from changemaker import views as changemaker
from associate import views as associate


def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']

        subject = 'Query from ' + name
        message = 'Hi Social Vision, ' + query
        # send an email

        send_mail(subject, message, email, ['contact.socialvision@gmail.com'])

        # impacts = Impact.objects.all()

        context = {
            'name': name,
            # 'impacts': impacts,
        }
    else:
        # impacts = Impact.objects.all()

        context = {
            # 'impacts': impacts,
        }

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


def impact(request):

    # impacts = Impact.objects.all()

    context = {
        # 'impacts': impacts,
    }

    return render(request, 'main/impact.html', context)


def gallery(request):

    events = Event.objects.all()
    trainees = trainee.getTrainees()
    changemakers = changemaker.getChangeMakers()

    context = {
        'events': events,
        'trainees': trainees,
        'changemakers': changemakers,
    }

    return render(request, 'main/gallery.html', context)


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


def profile(request):
    user = request.user

    groups = None
    isChangeMaker = False
    isTrainee = False

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
        'isChangeMaker': isChangeMaker,
        'isTrainee': isTrainee,
    }

    return render(request, 'main/profile.html', context)


@allowed_users(allowed_roles=['changemaker'])
def finance(request):
    user = request.user

    # instantDonations = instantDonations()
    cmDonations = changemaker.getDonation()
    asDonations = associate.getDonations()
    asExpenses = associate.getExpenses()
    asFees = associate.getServiceFees()

    cmDonationSum = 0
    asDonationSum = 0
    asExpenseSum = 0
    asFeeSum = 0

    for don in cmDonations:
        cmDonationSum += don.amount

    for don in asDonations:
        asDonationSum += don.amount

    for don in asExpenses:
        asExpenseSum += don.amount

    for don in asFees:
        asFeeSum += don.amount

    context = {
        'user': user,
        'changemakerDonations': cmDonations,
        'associateDonations': asDonations,
        'associateExpenses': asExpenses,
        'associateFees': asFees,
        'cmDonationSum': cmDonationSum,
        'asDonationSum': asDonationSum,
        'asExpenseSum': asExpenseSum,
        'asFeeSum': asFeeSum,
    }

    return render(request, 'main/finance.html', context)


@allowed_users(allowed_roles=['admin'])
def panel(request):

    users = User.objects.all()
    trainees = trainee.getTrainees()
    changemakers = changemaker.getChangeMakers()
    associates = associate.getAssociates()

    context = {
        'users': users,
        'trainees': trainees,
        'changemakers': changemakers,
        'associates': associates,
    }

    return render(request, 'main/panel.html', context)


def newsletter(request):

    return render(request, 'main/newsletter.html')
