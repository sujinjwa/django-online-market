from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password # 암호화된 비밀번호와 비교
from django.contrib import messages
from .models import Member

# Create your views here.

# 로그인 페이지
def login(request):

    # 기능 2 : 아이디, 비번 입력 받아서 로그인하기
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        # DB 내 유저의 정보와 입력 받은 정보 비교하여 로그인 여부 결정
        if Member.objects.filter(user_id=user_id).exists():
            member = Member.objects.get(user_id=user_id)

            # 암호화된 비밀번호와 member의 비밀번호 일치하는지 확인
            if check_password(password, member.password):
                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')

        # 로그인 실패!
        

    # 기능 1 : 로그인 화면 출력
    return render(request, 'login.html')

    # 아이디,비번 입력 받아서 redirect하는 것까지!

def logout(request):
    # 로그인 되어 있는 유저만 로그아웃 가능하도록 
    if 'user_pk' in request.session:
        # del: dictionary 형태의 데이터 삭제하는 메서드
        del(request.session['user_pk'])
    if 'user_id' in request.session:
        del(request.session['user_id'])

    return redirect('/')

def register(request):
    if request.method == 'POST':
        if Member.objects.filter(user_id=request.POST.get('user_id')).exists():
            messages.info(request, '동일한 아이디가 존재합니다.')
            return redirect('/member/register')

        member = Member(
            user_id = request.POST.get('user_id'),
            password = make_password(request.POST.get('password')),
            name = request.POST.get('name'),
            age = request.POST.get('age'),
        )
        member.save()
        return redirect('/member/login/nn')
    
    return render(request, 'register.html')