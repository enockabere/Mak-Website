from django.contrib import admin

from about.models import AboutUs, Personel, Mission, MDsMessage


class PersonelAdmin(admin.ModelAdmin):
    # # fields= [
    #     'first_name', 
    #     'middle_name', 
    #     'last_name',
    #     'profile_photo',
    #     'posuition',
    #     'status',
    #     'category',
    # # ]

    list_display = [
         'first_name', 
        'middle_name', 
        'last_name',
        # 'profile_photo',
        # 'posuition',
        # 'status',
        # 'category',
    ]


# Register your models here.
admin.site.register(AboutUs)
admin.site.register(Personel, PersonelAdmin)
admin.site.register(Mission)
admin.site.register(MDsMessage)