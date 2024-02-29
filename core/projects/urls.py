from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('create/', views.handle_project, name='new_project'),
    path('update/<project_id>/', views.handle_project, name='update_project'),
    path('detail/<project_id>/', views.project_datail, name='project_detail'),
    path('list/', views.project_list, name='project_list'),
    path('list/<category>/', views.project_list, name='project_list_category'),

]