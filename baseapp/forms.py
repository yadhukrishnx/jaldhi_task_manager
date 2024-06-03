from django import forms

from .models import Task,UserProfile

from django.contrib.auth.models import User

class Taskform(forms.ModelForm):
    
    class Meta:
        model = Task
        fields=['title','description']
        
        widgets={
            'title':forms.TextInput(attrs={'class':'formcontrol','placeholder':'Enter Task name'}),
            'description':forms.Textarea(attrs={'class':'formcontrol1','placeholder':'Enter Task Description'}),
        }
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
