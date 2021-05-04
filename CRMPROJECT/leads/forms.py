from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Lead

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
       model = Lead
       fields = (
           'first_name',
           'last_name',
           'age',
           'agent',
       )

class LeadForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0)

class CustomUserCreationForm(UserCreationForm):
    class  Meta:
       model = User
       fields = ('username',)
       field_classes = { 'username':UsernameField }