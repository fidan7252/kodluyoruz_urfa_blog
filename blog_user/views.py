from django.shortcuts import render
from django.contrib.auth import authenticate, login


def login_user(request):
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
            print('login oldun')
        else:
            print('login olamadin')
    return render(request, 'blog_user/login.html', {})