from django import forms
from django.contrib import auth


class LoginForm(forms.Form):
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

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if not auth.authenticate(username=username, password=password):
            self.add_error('password', '用户名或密码错误')
        return self.cleaned_data
