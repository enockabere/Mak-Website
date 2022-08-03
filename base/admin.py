from django.contrib import admin
from django.contrib.auth.models import Group
from base.models import Carousel,Patner, Subscription, CallToActionPanel

# Register your models here.

admin.site.register(Carousel)
admin.site.register(Patner)
admin.site.register(Subscription)
admin.site.register(CallToActionPanel)


# Dashboad Customization
admin.site.site_header = "MCSCUA Dashboard"
admin.site.unregister(Group)
