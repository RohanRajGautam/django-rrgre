from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def login(request):
  if request.method == 'POST':
    messages.error(request, 'Testing error message')
    return redirect('login')
  else:
    return render(request, 'accounts/login.html')

def register(request):
  if request.method == 'POST':
    # Register User
    return
  else:
    return render(request, 'accounts/register.html')

def logout():
  return redirect('index')

def dashboard(request):
  return render(request, 'accounts/dashboard.html')