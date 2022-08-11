from dataclasses import fields
from django.contrib import admin

from about.models import AboutUs, Personel, Mission, MDsMessage, Department
from django_summernote.admin import SummernoteModelAdmin



class AboutUsAdmin(SummernoteModelAdmin):
    fields = ('description', 'status')
    list_display = ['short_description', 'status']
    list_display_links = ['short_description']


class PersonelAdmin(SummernoteModelAdmin):

    fields = (
        'first_name',
        'middle_name',
        'last_name',
        'position',
        'description',
        'image',
        'category',
        'status'
     )

    list_display = [
        'profile_photo',
        'full_name',
        'short_description',
        'status',
    ]
    list_display_links = ['full_name']
    list_filter = ["status", 'category']
    search_fields = [
        'first_name',
        'middle_name',
        'last_name',
    ]

class MDsMessageAdmin(SummernoteModelAdmin):
    fields = (
        'image', 
        'title',  
        'message',
        'name_of_md', 
        'position', 
        'status'
    )

    list_display = [
        'profile_photo',
        'title',
        'name_of_md',
        'status',
    ]
    list_display_links = ['title','name_of_md']
    list_filter = ["status", ]
    search_fields = ['name_of_md',]
    
class DepartmentAdmin(SummernoteModelAdmin):
    list_display = ['title', 'short_content', 'status']
    list_filter = ['status']

# Register your models here.
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Personel, PersonelAdmin)
admin.site.register(Mission)
admin.site.register(MDsMessage, MDsMessageAdmin)
admin.site.register(Department, DepartmentAdmin)
