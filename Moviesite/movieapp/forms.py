#coding=utf-8
from django import forms

class SearchForm(forms.Form):
    moviename = forms.CharField(label='搜一搜', max_length=20)

class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


