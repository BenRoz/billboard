from django import forms
from django.shortcuts import render
from django.contrib.auth import (authenticate,
                                 get_user_model,
                                login, logout,
                                 )

User=get_user_model()

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("this user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("incorrect password")
            if not user.is_active:
                raise forms.ValidationError("this user is no longer active")
        return super(UserLoginForm, self).clean()

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password')


    class Meta:
        model=User
        fields=[   #can chage the field order
            'username',
            'password',
            'password2',

        ]