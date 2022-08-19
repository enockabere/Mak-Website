from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display= ['name', 'subject', 'pub_date']
    list_filter = ['pub_date',]
    search_fields = ['name', 'subject']

# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)