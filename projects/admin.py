from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ['photo', 'title', 'pub_date', 'status']
    list_display_links= ['title', 'photo']
    list_filter = ['pub_date', 'status']
    search_fields = ['title', 'description']

# Register your models here.
admin.site.register(Project, ProjectAdmin)