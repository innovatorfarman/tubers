from urllib.parse import uses_relative
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request,"Invalid Credentials")
    return render(request, 'accounts/login.html')



def signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"Username Already Exists!")
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request,"Email Already Exists")
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                    username=username, password=password)
                    user.save()
                    messages.success(request, "Account created Successfully!")
                  
        else:
            messages.warning(request, "Password does not match!")
    return render(request, 'accounts/signup.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

