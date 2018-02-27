from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect

User = get_user_model()

# 장고가 쓰고있는 user_model을 가져온다.


__all__ = (
    'logout_view',
)


def logout_view(request):
    logout(request)
    return redirect('index')
