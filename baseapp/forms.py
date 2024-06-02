from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    
    class Meta:
        model = Task
        fields=['title','description']
        
        widgets={
            'title':forms.TextInput(attrs={'class':'formcontrol','placeholder':'Enter Task name'}),
            'description':forms.Textarea(attrs={'class':'formcontrol1','placeholder':'Enter Task Description'}),
        }