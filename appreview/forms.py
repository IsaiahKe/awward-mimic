from django.contrib.auth.models import User
from django import forms

from .models import AppVote, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('last_name','first_name')
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('bio','userPhoto','contact','location')
        
        
        
class ProjectForm(forms.ModelForm):
    class Meta:
        model=AppVote
        exclude=['author','usability','content','design','total']
class ProjectVote(forms.ModelForm):
    class Meta:
        model=AppVote
        exclude=['author','total','livelink','total','appimage','appname']
        