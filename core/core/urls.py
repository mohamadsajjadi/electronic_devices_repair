from django.contrib import admin
from django.urls import path, include
from user.views import home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('user.urls'), name='accounts'),
    path('project/', include('projects.urls'), name='projects'),
    path('offer/', include('offer.urls'), name='offer'),
]
