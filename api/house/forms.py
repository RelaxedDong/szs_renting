#encoding:utf-8

from django import forms
from django.core import validators
from .models import House


class SearchForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['subway','house_type','region']
