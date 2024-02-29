
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from projects.models import Project, ProjectStatus
from .models import Offer, OfferStatus
from .forms import CreateOfferForm
# Create your views here.

@login_required
def create_offer(request, project_id):
    if request.user.role != 'REP':
        return HttpResponse('Forbidden', status=403)

    form = CreateOfferForm()
    project = get_object_or_404(Project, id=project_id)
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
    project = get_object_or_404(Project ,id=project_id)

    has_already_accepted = project.project_offer.filter(status=OfferStatus.accepted)
    if has_already_accepted:
        return redirect(reverse_lazy("projects:project_list"))
    
    offers = project.project_offer.filter(status=OfferStatus.pending)
    return render(request, 'offer/offer_list.html', {'offers' : offers, 'project' : project})

def change_offer(request, offer_id, change):
    offer_obj = Offer.objects.get(id=offer_id)
    project_obj = Project.objects.get(id=offer_obj.project_id.id)

    if project_obj.employer != request.user:
        return HttpResponse('forbidden', status=403)
        
    if change == 'accept':
        project_obj.status = ProjectStatus.taken
        offer_obj.status = OfferStatus.accepted
    if change == 'reject':
        offer_obj.status = OfferStatus.rejected

    offer_obj.save()
    project_obj.save()

    return redirect(reverse_lazy("projects:project_list"))
    