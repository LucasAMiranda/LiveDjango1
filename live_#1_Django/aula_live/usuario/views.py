from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .models import Usuario
import json

# Create your views here.

def cadastro(request):
    return HttpResponse(json.dumps({"name": "Lucas"}))

def login(request):
    status = request.GET.get("status")
    return render(request, 'login/login.html', {'status': status})

def home(request):
    return HttpResponse("Você está na página home")

def salvar(request):
    try:
        nome = request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        idade = request.POST.get("idade")

        usuario = Usuario (
            nome = nome,
            sobrenome = sobrenome,
            idade = idade
        )
    
        return redirect("/usuario/login/?status=1")
    except:
          return redirect("/usuario/login/?status=2")

    #return HttpResponse(f"{nome} {sobrenome} {idade}")
