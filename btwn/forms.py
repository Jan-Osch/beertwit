# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import UserProfile


class UserForm(forms.ModelForm):
    password_confirmation = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        exclude = []

    def clean_password_confirmation(self):
        confirmation = self.cleaned_data['password_confirmation']
        password = self.cleaned_data['password']
        if confirmation != password:
            raise ValidationError('Passwords do not match')
        return confirmation

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise ValidationError('Username already taken.')
        return data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']

    def clean_profile_name(self):
        data = self.cleaned_data['profile_name']
        if UserProfile.objects.filter(profile_name=data).exists():
            raise ValidationError("Profile name already taken")
        return data
