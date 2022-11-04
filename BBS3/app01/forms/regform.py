from django import forms
from app01 import models


class RegForm(forms.Form):
    username = forms.CharField(
        label='用户名', min_length=3, max_length=32,
        error_messages={
            'min_length': '用户名不能小于3位',
            'max_length': '用户名不能打于32位',
            'required': '用户名不能为空',
        },
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='密码', min_length=3, max_length=32,
        error_messages={
            'min_length': '密码不能小于3位',
            'max_length': '密码不能打于32位',
            'required': '密码不能为空',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        label='确认密码', min_length=3, max_length=32,
        error_messages={
            'min_length': '确认密码不能小于3位',
            'max_length': '确认密码不能打于32位',
            'required': '确认密码不能为空',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'required': '邮箱不能为空',
            'invalid': '邮箱格式不合法'
        },
        widget = forms.widgets.EmailInput(attrs={'class': 'form-control'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if models.UserInfo.objects.filter(username=username):
            self.add_error('username', '用户名已存在')
        return username

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not password == confirm_password:
            self.add_error('confirm_password', '两次密码不一致')
        return self.cleaned_data
