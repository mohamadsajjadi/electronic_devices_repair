from django.contrib import admin
from .models import Project, Category, Offer
# Register your models here.

admin.site.register(Offer)
admin.site.register(Project)
admin.site.register(Category)
