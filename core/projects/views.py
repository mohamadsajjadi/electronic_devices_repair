from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Project, ProjectStatus
from .forms import CreateProjectForm
# Create your views here.

@login_required
def handle_project(request, project_id=None):
    if request.user.role != 'CUS':
        return HttpResponse('Forbidden', status=403)

    project_obj = None
    title = 'Create a new project'
    if project_id :
        project_obj = Project.objects.get(id=project_id)
        title = 'Update your project'
    form = CreateProjectForm(instance=project_obj)

    if request.method == "POST":
        form = CreateProjectForm(request.POST, instance=project_obj)
        if form.is_valid():
            project = form.save(commit=False)
            project.employer = request.user
            project.save()
            return redirect(reverse_lazy('home'))
    return render(request, 'project/project.html', {'form' : form, 'title' : title})

@login_required
def delete_project(request, project_id):
    error = False
    project = Project.objects.get(id=project_id)

    if project:
        error = 'project doesn\'t exist'

    if request.user.id != project.employer.id:
        error = 'bad request'
    
    if not error:
        project.delete()

    return redirect(reverse_lazy('hone'))

def project_datail(request, project_id):
    project_obj = Project.objects.get(id=project_id)
    return render(request, 'project/project_detail.html', {'project' : project_obj})

def project_list(request, category=None):
    mine = request.GET.get('mine')
    
    projects_obj = Project.objects.filter(status=ProjectStatus.in_process)

    try:
        if category:
            projects_obj = projects_obj.filter(category=category)
    except:
        projects_obj = None

    if mine:
        projects_obj = projects_obj.filter(employer=request.user)

    return render(request, 'project/project_list.html', {'projects' : projects_obj})