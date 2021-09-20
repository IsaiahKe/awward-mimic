from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from .models import AppVote

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('last_name',)
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model=AppVote
        exclude=['author','usability','content','design','total']
        