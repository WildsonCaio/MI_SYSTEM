from django.shortcuts import render, redirect
from django.contrib import auth

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        authentication = auth.authenticate(request, username=email, password=password)
        
        if authentication is not None:
            auth.login(request, authentication)
            return redirect('home')
            
        
        
        
    else:    
        return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')
