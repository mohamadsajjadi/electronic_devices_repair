from  django import forms
from .models import Project

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('employer', 'published_at', 'done_at')
