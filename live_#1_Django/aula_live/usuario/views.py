from django.shortcuts import render
from django.http import  HttpResponse
import json

# Create your views here.

def cadastro(request):
    return HttpResponse(json.dumps({"name": "Lucas"}))

def login(request):
    nome = request.GET.get("nome")
    sobrenome = request.GET.get("sobrenome")
    return render(request, 'login/login.html', {'nome_usuario': nome, 'sobrenome': sobrenome})

def home(request):
    return HttpResponse("Você está na página home")
