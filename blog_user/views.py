from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(
                request, username=username,
                password=password
            )
            print(user)
            if user is not None:
                login(request, user)
                messages.add_message(
                    request, messages.SUCCESS, 
                    f'Hosgeldin {username}'
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


def sign_up(request):
    if request.method == "POST":
        r_post = request.POST
        username = r_post.get('email')
        password = r_post.get('password')
        password2 = r_post.get('password2')
        if username and (password == password2):
            user = User.objects.create_user(
                username, 
                username, 
                password
            )
            auth = authenticate(
                request, username=username,
                password=password
            )
            login(request, auth)
            return redirect('home')

    return render(request, 'blog_user/sign_up.html',{})
