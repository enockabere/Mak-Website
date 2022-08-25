from django.contrib import admin
from resources.models import Faq, Publication, Privacy,Terms
from django_summernote.admin import SummernoteModelAdmin


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['name', ]


class FaqAdmin(SummernoteModelAdmin):
    list_display = ('question', 'short_description', 'status')
    list_filter = ['date_created', ]
    search_fields = ['question', 'answer']

class PrivacyAdmin(SummernoteModelAdmin):
    list_display = ['title', 'modified', 'status']

class TermsAdmin(SummernoteModelAdmin):
    list_display = ['title', 'modified', 'status']

class PublicationAdmin(admin.ModelAdmin):
    list_display= ['name', 'pub_date', 'category', 'status']

# Register your models here.
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Terms, TermsAdmin)
admin.site.register(Privacy, PrivacyAdmin)
