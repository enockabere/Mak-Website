from django.contrib import admin
from resources.models import Faq, JobAdvert, Publication, Tender
from django_summernote.admin import SummernoteModelAdmin




class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name',]



class JobAdvertAdmin(SummernoteModelAdmin):
    summernote_fields = ['qualification','resposibilities']

    fields = (
        'title', 
        'slug', 
        'job_ID', 
        'job_description', 
        'qualification', 
        'resposibilities', 
        'advert_file', 
        'job_type', 
        'status'
    )

    list_display = ('title', 'job_ID', 'short_description', 'job_type', 'status')
    list_display_links = ('title', 'job_ID')
    list_filter = ('pub_date',)
    search_fields = ('title', 'job_ID')
    prepopulated_fields = {'slug':('title', 'job_ID')}


class FaqAdmin(SummernoteModelAdmin):
    list_display = ('question', 'short_description', 'status')
    list_filter = ['date_created', ]
    search_fields = ['question', 'answer']

class TenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'ref_number', 'short_description', 'status')
    list_filter = ('pub_date',)

# Register your models here.
admin.site.register(Publication)
admin.site.register(Faq, FaqAdmin)
admin.site.register(JobAdvert, JobAdvertAdmin)
admin.site.register(Tender, TenderAdmin)