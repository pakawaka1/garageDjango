from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def user(request):
    return render(request, 'user.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        # email= request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user')
        else: 
            return redirect('login')
    else:
        return render(request, 'login.html',{})
