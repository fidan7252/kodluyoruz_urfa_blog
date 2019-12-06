from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    if request.method == "POST":
        user_name = request.POST.get('email')
        password = request.POST.get('password')
        if user_name and password:
            user = authenticate(
                request, username=user_name,
                password=password
            )
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print('login olamadin')
    return render(request, 'blog_user/login.html', {})\


def logout_user(request):
    logout(request)
    return redirect('home')