from django.contrib import admin
from about.models import AboutUs, Personel, Mission, MDsMessage, Department, Functions, Objectives, Vision, ServiceCharter
from django_summernote.admin import SummernoteModelAdmin


class AboutUsAdmin(SummernoteModelAdmin):
    fields = ('description', 'status')
    list_display = ['title', 'status']
    list_display_links = ['title']


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
        'category',
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
        'title',
        'name_of_md',
        'status',
    ]
    list_display_links = ['title', 'name_of_md']
    list_filter = ["status", ]
    search_fields = ['name_of_md', ]


class DepartmentAdmin(SummernoteModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']


class FunctionsAdmin(SummernoteModelAdmin):
    list_display = ['title', 'status']


class ObjectivesAdmin(SummernoteModelAdmin):
    list_display = ['title', 'status']


class VisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']


class MissionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']


class ServiceCharterAdmin(SummernoteModelAdmin):
    list_display = ['title', 'status']


# Register your models here.
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Personel, PersonelAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(MDsMessage, MDsMessageAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Functions, FunctionsAdmin)
admin.site.register(Objectives, ObjectivesAdmin)
admin.site.register(Vision, VisionAdmin)
admin.site.register(ServiceCharter, ServiceCharterAdmin)
