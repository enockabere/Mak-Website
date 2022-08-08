from django.contrib import admin
from resources.models import Faq, JobAdvert


class JobAdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'job_ID', 'job_type')
    list_filter = ('pub_date',)
    search_fields = ('title', 'job_ID')
    prepopulated_fields = {'slug':('title', 'job_ID')}


# Register your models here.
admin.site.register(Faq)
admin.site.register(JobAdvert, JobAdvertAdmin)