from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistration
from django.contrib import messages

def index(request):
    return render(request, 'main.html')

def register(request):
    if request.method == "POST":
        request_form = UserRegistration(request.POST)
        if request_form.is_valid():
            request_form.save()
            messages.success(request,("Registraion has been completed succesfully, login to proceed."))
    reg_form = UserRegistration()
    return render(request,'register.html', {'reg_form' : reg_form})
