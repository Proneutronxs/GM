from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db import connections
from django.http import JsonResponse
from django.http import HttpResponse, Http404

# Create your views here.


def LogIn (request):
    return render (request, 'Main/Login/login.html')

@login_required
def GM(request):
    return render (request, 'Main/Main/index.html')

@login_required
def verPlus(request):
    return render (request, 'Main/Plus/verPlus.html')

@csrf_exempt
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            data = "Se inicio sesion."
            return JsonResponse({'Message': 'success', 'data': data})
        else:
            data = "No se pudo iniciar sesión, verifique los datos."
            return JsonResponse({'Message': 'Error', 'data': data})
    else:
        data = "No se pudo resolver la Petición"
        return JsonResponse({'Message': 'Error', 'Nota': data})