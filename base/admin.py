from django.contrib import admin
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin
from base.models import Carousel, Patner, Subscription, CallToActionPanel


class CarouselAdmin(admin.ModelAdmin):
    fields = (
        'image',
        'photo',
        'title',
        'caption',
        'status',
    )

    list_display = [
        'photo',
        'title',
        'short_description',
        'status',
        'created_on',
    ]
    list_display_links = ['title']
    list_filter = ['status', 'created_on']
    search_fields = ['title', 'caption']
    readonly_fields = ['photo', 'created_on', ]


class PatnerAdmin(admin.ModelAdmin):

    fields = ('image', 'name', 'caption', 'url', 'status')

    list_display = [
        'org_photo',
        'name',
        'short_description',
        'status',
    ]

    list_display_links = ['name']
    list_filter = ['status', ]
    search_fields = ['name', 'caption']


class CallToActionPanelAdmin(admin.ModelAdmin):
    fields = ('image', 'title', 'url', 'description', 'status')

    list_display = [
        'photo',
        'title',
        'short_description',
        'status',
    ]
    list_display_links = ['title']
    list_filter = ["status",]
    search_fields = ['title', 'description']

# Register your models here.
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Patner, PatnerAdmin)
admin.site.register(Subscription)
admin.site.register(CallToActionPanel, CallToActionPanelAdmin)


# Dashboad Customization
admin.site.site_header = "MCSCUA Dashboard"
admin.site.unregister(Group)
