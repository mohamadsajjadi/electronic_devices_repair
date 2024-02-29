from django.contrib import admin
from .models import Project, Category
from offer.models import Offer
# Register your models here.

class OfferInline(admin.StackedInline):
    model = Offer
    extra = 0
    show_change_link = True

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['employer', 'title', 'status', 'expected_price', 'expected_time']
    list_filter = ('employer__phone_number', 'created_at', 'category')
    search_fields = ('content__icontains',)
    inlines = [OfferInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
