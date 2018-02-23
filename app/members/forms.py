from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()
__all__ = (
    'SignupForm'
)


class SignupForm(forms.Form):
    username = forms.CharField(label='아이디')
    password = forms.CharField(label='비밀번호',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(label='비밀번호 확인',
        widget=forms.PasswordInput
    )

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError('이미 사용중인 아이디입니다.')
        return data

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError('비밀번호가 일치하지 않습니다.')
        return password2