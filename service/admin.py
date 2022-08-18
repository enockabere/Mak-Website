from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status', ]
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Service, ServiceAdmin)
