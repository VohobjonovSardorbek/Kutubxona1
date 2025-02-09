from django import forms
from flask import request
from telebot.apihelper import forward_message

from .models import *

class TalabaForm(forms.ModelForm):
    class Meta:
        model = Talaba
        fields = '__all__'


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'


class Kitobform(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'