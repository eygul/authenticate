from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from user.forms import UserCreationForm
from django.contrib import messages
from .models import CustomUser

def home(request):
    return render(request, 'user/home.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'user/register.html', {'form': form})

    

def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email OR password is incorrect')
    context = {}
    return render(request, 'user/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('home')