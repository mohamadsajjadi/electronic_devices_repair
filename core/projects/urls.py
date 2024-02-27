from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('create/', views.handle_project, name='new_post'),
    path('update/<project_id>', views.handle_project, name='update_project'),
    path('<project_id>/', views.project_datail, name='project_detail'),
    path('list', views.project_list, name='project_list'),
]