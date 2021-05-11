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
@allowed_users(allowed_roles=['trainee'])
def traineeProfile(request):
    user = request.user
    try:
        cd = Trainee.objects.get(user=user)
        context = {
            'user':user,
            'cd':cd,
        }
    except ObjectDoesNotExist as o:
        context = {
            'user':user,
        }


    return render(request, 'trainee/traineeUser.html', context)

@authenticated_user
def regTrainee(request):
    user = request.user
    form = TraineeForm(initial={'user': request.user.id})

    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            trainee = form.save()   
            add_group = Group.objects.get(name='trainee') 
            add_group.user_set.add(request.user)
            return redirect('/trainee/edit/')

    context = {
        'form': form,
    }

    return render(request, 'trainee/regTrainee.html', context)

@authenticated_user
@allowed_users(allowed_roles=['trainee'])
def editTrainee(request):
    user = request.user

    cd = Trainee.objects.get(user=user)
    form = TraineeForm(instance=cd)

    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES, instance=cd)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'cd': cd,
        'form': form,
    }

    return render(request, 'trainee/editTrainee.html', context)

@authenticated_user
@allowed_users(allowed_roles=['trainee'])
def printTraineeForm(request):

    user = request.user
    cd = Trainee.objects.get(user=user)
    form = TraineeForm(instance=cd)

    context = {
        'cd': cd,
    }

    template_path = 'trainee/traineeForm.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Trainee-Form.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@authenticated_user
@allowed_users(allowed_roles=['trainee'])
def printTraineeID(request):

    user = request.user
    cd = Trainee.objects.get(user=user)
    form = TraineeForm(instance=cd)

    context = {
        'cd': cd,
    }

    template_path = 'trainee/traineeID.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Trainee-ID.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

