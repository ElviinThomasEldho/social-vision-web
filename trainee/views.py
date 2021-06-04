from django.db.models.expressions import OrderBy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

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
def profile(request):
    user = request.user

    tr = Trainee.objects.get(user=user)
    courses = Course.objects.all
    enrollments = Enrollment.objects.order_by(
        'startDate').filter(trainee=tr).reverse()

    context = {
        'user': user,
        'courses': courses,
        'enrollments': enrollments,
        'tr': tr,
    }

    return render(request, 'trainee/profile.html', context)


@authenticated_user
def register(request):
    user = request.user
    form = TraineeForm(initial={'user': request.user.id})

    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            trainee = Trainee.objects.get(user=request.user)
            trainee.firstName = user.first_name
            trainee.lastName = user.last_name
            trainee.emailID = user.email

            today = date.today()
            trainee.age = today.year - trainee.dateOfBirth.year - \
                ((today.month, today.day) <
                 (trainee.dateOfBirth.month, trainee.dateOfBirth.day))
            trainee.save()
            add_group = Group.objects.get(name='trainee')
            add_group.user_set.add(request.user)
            return redirect('/trainee/edit/')

    context = {
        'form': form,
    }

    return render(request, 'trainee/register.html', context)


@authenticated_user
@allowed_users(allowed_roles=['trainee'])
def edit(request):
    user = request.user
    tr = Trainee.objects.get(user=user)
    form = TraineeForm(instance=tr)

    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES, instance=tr)
        if form.is_valid():
            form.save()
            return redirect('trainee')

    context = {
        'tr': tr,
        'form': form,
    }

    return render(request, 'trainee/edit.html', context)


@authenticated_user
@allowed_users(allowed_roles=['trainee'])
def printForm(request):

    user = request.user
    tr = Trainee.objects.get(user=user)
    form = TraineeForm(instance=tr)
    enrollments = Enrollment.objects.filter(trainee=tr)

    context = {
        'tr': tr,
        'enrollments': enrollments,
    }

    template_path = 'trainee/printForm.html'
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
def printID(request):

    user = request.user
    tr = Trainee.objects.get(user=user)
    enrollments = Enrollment.objects.filter(trainee=tr)

    context = {
        'tr': tr,
        'enrollments': enrollments,
    }

    template_path = 'trainee/printID.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="Trainee-ID.pdf'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def getTrainees():
    users = Trainee.objects.all()
    return users


def activate(request, id):
    trainee = Trainee.objects.get(uniqueID=id)
    trainee.status = True
    trainee.save()

    name = trainee.firstName + ' ' + trainee.lastName
    email = trainee.emailID
    query = "Hi " + name + ", We are happy to inform you that your Trainee Account has been activated. You can now download you ID Card from the Trainee Profile Page"

    subject = 'Query from ' + name
    message = 'Hi Social Vision, ' + query
    # send an email

    send_mail(subject, message, 'contact.socialvision@gmail.com', [email])

    context = {
        'name': name,
    }

    return redirect('/admin-panel/')


def deactivate(request, id):
    trainee = Trainee.objects.get(uniqueID=id)
    trainee.status = False
    trainee.save()

    return redirect('/admin-panel/')


def enroll(request, id):
    user = request.user
    trainee = Trainee.objects.get(user=user)
    course = Course.objects.get(id=id)

    if Enrollment.objects.filter(trainee=trainee, course=course):
        return redirect('trainee')
    else:
        endDate = datetime.date.today()
        duration = course.duration
        if (endDate.month + duration) > 12:
            endDate = endDate.replace(month=endDate.month + duration -
                                      12, year=endDate.year + 1)

        else:
            endDate = endDate.replace(month=endDate.month + duration)

        enrollment = Enrollment.objects.create(
            trainee=trainee,
            course=course,
            startDate=datetime.date.today(),
            endDate=endDate,
        )

        lastCourse = Enrollment.objects.filter(
            trainee=trainee).order_by('endDate').last()

        validUpto = lastCourse.endDate

        return redirect('/trainee/view/')


def unenroll(request, id):
    trainee = Trainee.objects.get(user=request.user)

    Enrollment.objects.get(id=id).delete()

    try:
        lastCourse = Enrollment.objects.filter(
            trainee=trainee).order_by('endDate').last()
        validUpto = lastCourse.endDate
    except AttributeError:
        validUpto = datetime.date.today()

    trainee.save()

    return redirect('/trainee/view/')
