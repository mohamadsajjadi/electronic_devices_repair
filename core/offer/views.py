
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import CreateOfferForm
# Create your views here.

@login_required
def create_offer(request, project_id):
    form = CreateOfferForm()
    project = Project.objects.get(id=project_id)

    if request.method == "POST":
        form = CreateOfferForm(request.POST)
        if form.is_valid():
            offer = form.save(commit=False)
            offer.service_man = request.user
            offer.project_id = project
            offer.save()
            return redirect(reverse_lazy('projects:project_detail', kwargs={'project_id': project_id}))
    return render(request, 'offer/create_offer.html', {'form' : form, 'project' : project})

@login_required
def offers_list(request, project_id):
    project = Project.objects.get(id=project_id)
    offers = project.project_offer.all()
    return render(request, 'offer/offer_list.html', {'offers' : offers, 'project' : project})