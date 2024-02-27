from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreateOfferForm
# Create your views here.

def create_offer(request):
    form = CreateOfferForm()
    if request.method == "POST":
        form = CreateOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.service_man = request.user
            offer.save()
            return redirect(reverse_lazy())
    return render(request, 'offer/handle_offer.html', {'form' : form})

def check_offer(request):
    pass