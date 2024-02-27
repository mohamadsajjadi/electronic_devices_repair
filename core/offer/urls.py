from django.urls import path
from . import views

app_name = 'offer'


urlpatterns = [
    path('create/', views.create_offer, name='create_offer'),
]
