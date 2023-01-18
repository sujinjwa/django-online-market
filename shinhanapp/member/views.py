from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password # 암호화된 비밀번호와 비교
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def signin(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        # authenticate : 인증 함수, 해당 user_id, pw 가지는 유저 있는가 여부 확인
        user = authenticate(request, username=user_id, password=password)
        if user is not None: # 해당 조건 만족하는 유저가 있는 경우 로그인
            login(request, user) # login: django.contrib.auth 로부터 임포트된 외부 함수
            return redirect('/')

    # 기능 1 : 로그인 화면 출력
    return render(request, 'login.html')

def signout(request):
    logout(request) # logout: django.contrib.auth 로부터 임포트된 외부 함수
    return redirect('/')

def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            request.POST.get('user_id'),
            request.POST.get('email'),
            request.POST.get('password'),
        )
        return redirect('/member/login/')
    
    return render(request, 'register.html')