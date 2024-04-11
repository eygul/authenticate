from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from user.forms import UserCreationForm


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
    if request.user.is_authenticated:
        return render(request, 'user/home.html')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    
    return render(request, 'user/login.html', {'form': form})
    
def logoutPage(request):
    logout(request)
    return redirect('home')