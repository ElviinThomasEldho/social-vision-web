from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist

import datetime

from django.views.generic import View
from django.template.loader import get_template
from Social_Vision_Web.utils import render_to_pdf

import os
from django.conf import settings
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

from .decorators import *
from django.contrib.auth.models import Group


def link_callback(uri, rel):
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


@authenticated_user
def register(request):
    user = request.user
    form = ChangeMakerForm(initial={'user': request.user})

    if request.method == 'POST':
        form = ChangeMakerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            changemaker = ChangeMaker.objects.get(user=request.user)
            changemaker.firstName = user.first_name
            changemaker.lastName = user.last_name
            changemaker.emailID = user.email

            today = date.today()
            changemaker.age = today.year - changemaker.dateOfBirth.year - \
                ((today.month, today.day) <
                 (changemaker.dateOfBirth.month, changemaker.dateOfBirth.day))
            changemaker.save()

            add_group = Group.objects.get(name='changemaker')
            user = form.cleaned_data['user']
            add_group.user_set.add(user)
            return redirect('/change-maker/view/')

    context = {
        'form': form,
    }

    return render(request, 'changemaker/registerForm.html', context)


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def profile(request):
    user = request.user
    changemaker = ChangeMaker.objects.get(user=user)

    if user.donation_set.all():
        donations = user.donation_set.all()
    else:
        donations = False

    if user.monthlydonation_set.all():
        monthly = user.monthlydonation_set.all()
    else:
        monthly = False

    context = {
        'user': user,
        'changemaker': changemaker,
        'donations': donations,
        'monthly': monthly,
    }

    return render(request, 'changemaker/profile.html', context)


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def donationForm(request):
    user = request.user
    form = DonationForm(initial={'user': request.user})

    if request.method == 'POST':
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uniqueID = Donation.objects.latest('dateCreated').uniqueID
            return redirect('/change-maker/pay/' + str(uniqueID) + '/')

    context = {
        'form': form,
    }

    return render(request, 'changemaker/form.html', context)


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def payment(request, id):
    donation = Donation.objects.get(uniqueID=id).amount
    uniqueID = Donation.objects.get(uniqueID=id).uniqueID

    context = {
        'donation': donation,
        'id': uniqueID,
    }

    return render(request, 'changemaker/payment.html', context)


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def paymentSuccess(request, id):
    donation = Donation.objects.get(uniqueID=id)
    donation.status = "Completed"
    donation.save()

    return redirect('/change-maker/view/')


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def printCertificate(request, id):
    user = request.user
    dn = Donation.objects.get(uniqueID=id)

    context = {
        'dn': dn,
        'user': user,
    }

    template_path = 'changemaker/certificate.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Donation-Certificate.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def printReceipt(request, id):
    user = request.user
    dn = Donation.objects.get(uniqueID=id)

    context = {
        'dn': dn,
        'user': user,
    }

    template_path = 'changemaker/receipt.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Donation-Receipt.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def monthlyDonationForm(request):
    user = request.user
    form = MonthlyDonationForm(initial={'user': request.user})

    if request.method == 'POST':
        form = MonthlyDonationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            uniqueID = MonthlyDonation.objects.latest(
                'dateCreated').uniqueID
            return redirect('/change-maker/monthly/pay/' + str(uniqueID) + '/')

    context = {
        'form': form,
    }

    return render(request, 'changemaker/monthlyForm.html', context)


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def paymentMonthly(request, id):
    donation = MonthlyDonation.objects.get(uniqueID=id).amount
    uniqueID = MonthlyDonation.objects.get(uniqueID=id).uniqueID

    context = {
        'donation': donation,
        'id': uniqueID,
    }

    return render(request, 'changemaker/monthlyPayment.html', context)


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def paymentMonthlySuccess(request, id):
    donation = MonthlyDonation.objects.get(uniqueID=id)
    donation.status = "Completed"
    donation.save()

    return redirect('/change-maker/view/')


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def printMonthlyCertificate(request, id):
    user = request.user
    dn = MonthlyDonation.objects.get(uniqueID=id)

    context = {
        'dn': dn,
        'user': user,
    }

    template_path = 'changemaker/monthlyCertificate.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Monthly-Donation-Certificate.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


@authenticated_user
@allowed_users(allowed_roles=['changemaker'])
def printMonthlyReceipt(request, id):
    user = request.user
    dn = MonthlyDonation.objects.get(uniqueID=id)

    context = {
        'dn': dn,
        'user': user,
    }

    template_path = 'changemaker/monthlyReceipt.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Monthly-Donation-Receipt.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def getChangeMakers():
    changemakers = ChangeMaker.objects.all()
    return changemakers


def getDonation():
    donations = Donation.objects.all()
    return donations
