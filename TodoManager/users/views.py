from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import CoustomRegistrationForms
from django.contrib import messages
from django.contrib.auth import logout





# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CoustomRegistrationForms(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User registered successfully!")
            return redirect("todolist")
    else:    
        register_form = CoustomRegistrationForms()
    return render(request, "register.html", {'register_form': register_form})

def manual_logout(request: HttpRequest) -> HttpResponse:
    logout(request)
    return render(request, 'main.html')