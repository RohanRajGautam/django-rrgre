from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

def login(request):
  if request.method == 'POST':
    return
  else:
    return render(request, 'accounts/login.html')

def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:
      # Check username
      if User.objects.filter(username=username).exists():
        messages.error(request, 'Username is already taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Email is already registered')
          return redirect('register')
        else:
          # Looks good
          user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
          user.save()
          auth.login(request, user)
          messages.success(request, 'Successfully registered and logged in.')
          return redirect('index')
    else:
      messages.error(request, 'Password do not match')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')

def logout():
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')