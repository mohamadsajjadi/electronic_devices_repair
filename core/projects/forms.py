from  django import forms
from django.core.exceptions import ValidationError

from .models import Project, Offer

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('employer', 'published_at', 'done_at')


class CreateOfferForm(forms.Form):
    class Meta:
        model = Offer