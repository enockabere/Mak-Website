from atexit import register
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Project, ProjectCategory


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ['photo', 'title', 'pub_date', 'status']
    list_display_links= ['title', 'photo']
    list_filter = ['pub_date', 'status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
class ProjectCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category',)}

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)