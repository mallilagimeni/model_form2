from django import forms

from django.http import HttpResponse
from django.core import validators


def check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('Invalid')
         
def len_for(value):
    if len(value)<5:
        raise forms.ValidationError('not data')

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[validators.MaxLengthValidator(5)])
    age=forms.IntegerField(validators=[validators.MaxValueValidator(20)])
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False )
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError('invalid email')
        
    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('no enter')