from django.contrib import admin
from resources.models import Faq, Publication
from django_summernote.admin import SummernoteModelAdmin


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class FaqAdmin(SummernoteModelAdmin):
    list_display = ('question', 'short_description', 'status')
    list_filter = ['date_created', ]
    search_fields = ['question', 'answer']


# Register your models here.
admin.site.register(Publication)
admin.site.register(Faq, FaqAdmin)
