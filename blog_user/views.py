from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
                messages.add_message(
                    request, messages.SUCCESS, 
                    f'Hosgeldin {user_name}'
                )
                return redirect('home')
            else:
                messages.add_message(
                    request, messages.WARNING, 
                    'Giris Yapamadiniz'
                )
    return render(request, 'blog_user/login.html', {})\


def logout_user(request):
    logout(request)
    messages.add_message(
        request, messages.SUCCESS, 
        'Oturumu Kapattiniz'
    )
    return redirect('home')


# def sign_up(request):
