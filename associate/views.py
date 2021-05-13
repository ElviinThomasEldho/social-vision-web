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
@allowed_users(allowed_roles=['admin'])
def regAssociate(request):
    user = request.user
    form = AssociateForm(initial={'user': request.user})

    if request.method == 'POST':
        form = AssociateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save()
            add_group = Group.objects.get(name='associate') 
            user = form.cleaned_data['user']
            add_group.user_set.add(user)
            return redirect('/associate/profile/')

    context = {
        'form': form,
    }

    return render(request, 'associate/regAssociate.html', context)

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def profAssociate(request):
    user = request.user
    associate = Associate.objects.get(user=user)

    context = {
        'associate':associate
    }

    return render(request, 'associate/profAssociate.html', context)

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def viewExpense(request):
    user = request.user
    try:
        expenses = user.expense_set.all()
        context = {
            'user':user,
            'expenses':expenses,
        }
    except ObjectDoesNotExist as o:
        context = {
            'user':user,
        }


    return render(request, 'associate/viewExpense.html', context)

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def addExpense(request):
    user = request.user
    form = ExpenseForm(initial={'user': request.user})

    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewExpense')

    context = {
        'form': form,
    }

    return render(request, 'associate/addExpense.html', context)

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def printExpense(request):
    user = request.user
    try:
        expense = user.expense_set.all()
        context = {
            'user':user,
            'expense':expense,
        }
    except ObjectDoesNotExist as o:
        context = {
            'user':user,
        }

    # return render(request, 'benefactor/donateCertif.html', context)

    template_path = 'associate/expReport.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Expense-Report.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def printExpReceipt(request, id):
    user = request.user
    exp = Expense.objects.get(uniqueID=id)
    context = {
        'exp': exp,
        'user':user,
    }

    # return render(request, 'benefactor/donateCertif.html', context)

    template_path = 'associate/expReceipt.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Expense-Receipt.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def addService(request):
    user = request.user
    form = ServiceForm(initial={'user': request.user})

    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewRevenue')

    context = {
        'form': form,
    }

    return render(request, 'associate/addService.html', context)

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def printServReceipt(request, id):
    user = request.user
    serv = Service.objects.get(uniqueID=id)

    context = {
        'serv': serv,
        'user':user,
    }

    # return render(request, 'benefactor/donateCertif.html', context)

    template_path = 'associate/servReceipt.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Service-Fee-Receipt.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def viewRevenue(request):
    user = request.user

    try:
        revenue = user.revenue_set.all()
    except ObjectDoesNotExist as o:
        revenue = "false"

    try:
        services = user.service_set.all()
    except ObjectDoesNotExist as o:
        services = "false"

    context = {
        'user':user,
        'revenue':revenue,
        'services':services,
    }

    return render(request, 'associate/viewRevenue.html', context)

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def addRevenue(request):
    user = request.user
    form = RevenueForm(initial={'user': request.user})

    if request.method == 'POST':
        form = RevenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewRevenue')

    context = {
        'form': form,
    }

    return render(request, 'associate/addRevenue.html', context)

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def printRevenue(request):
    user = request.user
    rev_list = user.revenue_set.all()
    serv_list = user.service_set.all()

    context = {
        'rev_list': rev_list,
        'serv_list': serv_list,
        'user':user,
    }

    # return render(request, 'benefactor/donateCertif.html', context)

    template_path = 'associate/revReport.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Revenue-Report.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@authenticated_user
@allowed_users(allowed_roles=['associate'])
def printRevReceipt(request, id):
    user = request.user
    rev = Revenue.objects.get(uniqueID=id)

    context = {
        'rev': rev,
        'user':user,
    }

    template_path = 'associate/revReceipt.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Revenue-Receipt.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

