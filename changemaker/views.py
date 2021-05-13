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
def donateView(request):
    user = request.user
    try:
        donations = user.donation_set.all()
        context = {
            'user':user,
            'donations':donations,
        }
    except ObjectDoesNotExist as o:
        context = {
            'user':user,
        }


    return render(request, 'changemaker/donateUser.html', context)


@authenticated_user
def donateForm(request):
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

    return render(request, 'changemaker/donateForm.html', context)

@authenticated_user
def donatePay(request, id):
    donation = Donation.objects.get(uniqueID=id).amount
    uniqueID = Donation.objects.get(uniqueID=id).uniqueID

    context = {
        'donation':donation,
        'id':uniqueID,
    }

    return render(request, 'changemaker/donatePay.html',context)

@authenticated_user
def donateSuccess(request, id):
    donation = Donation.objects.get(uniqueID=id)
    donation.status = "Completed"
    donation.save()
    context = {

    }

    return redirect('/change-maker/view/')

@authenticated_user
def printDonationCertif(request, id):
    user = request.user
    dn = Donation.objects.get(uniqueID=id)

    context = {
        'dn': dn,
        'user':user,
    }

    # return render(request, 'changemaker/donateCertif.html', context)

    template_path = 'changemaker/donateCertif.html'
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
def printDonationReceipt(request, id):
    user = request.user
    dn = Donation.objects.get(uniqueID=id)

    context = {
        'dn': dn,
        'user':user,
    }

    template_path = 'changemaker/donateReceipt.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Donation-Receipt.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response