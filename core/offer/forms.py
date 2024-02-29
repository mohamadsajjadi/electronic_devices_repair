from django import forms
from .models import Offer

class CreateOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        exclude = ('service_man', 'project_id', 'status')        