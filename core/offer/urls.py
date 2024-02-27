from django.urls import path
from . import views

app_name = 'offer'


urlpatterns = [
    path('create/<project_id>', views.create_offer, name='create_offer'),
    path('list/<project_id>', views.offers_list, name='offers_list')
]
