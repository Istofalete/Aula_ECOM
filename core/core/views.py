from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def contato(request):
    if request.method == "GET":
        return render(request, "contato.html")
    if request.method == "POST":
        print(request.POST.get("nome")," entrou entrou em contato!")
        return render(request, "login.html")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST" and request.POST.get("senha") == "teste123":
        print("Usuário ",request.POST.get("email")," entrou com sucesso!")
        return render(request, "index.html")
    else:
        print("Usuário ",request.POST.get("email")," digitou a senha errada!")
        return HttpResponse("Usuário digitou a senha errada!")
    return HttpResponse("Ação não permitida")