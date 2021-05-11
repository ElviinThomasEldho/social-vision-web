from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('home')

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            groups = None
            if request.user.groups.exists(): 
                groups = set(group.name for group in request.user.groups.all())
                for group in groups:
                    if group in allowed_roles:
                        return view_func(request, *args, **kwargs)
            
            message = 'You are not authorized to view this page. Register as ' + ', '.join(allowed_roles) + ' to view this page.'   
            return HttpResponse(message)
        return wrapper_func
    return decorator

