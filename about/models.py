from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db import models
from blog.models import  STATUS
from ckeditor.fields import RichTextField

# Create your models here.

CATEGORY = [
    (0, 'Board of management'),
    (1, "Leadership")
]

class Personel(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True, help_text='Optional')
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='media',  null=True, blank=True, help_text = 'Image size should be in .jpg or .png')
    category = models.IntegerField(choices=CATEGORY, default=0, help_text='select Peronel membership title')
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Personel'

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.middle_name, self.last_name)

    def profile_photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

class MDsMessage(models.Model):
    title = models.CharField(max_length=200, help_text="e.g. John's Message")
    message = RichTextField()
    image = models.ImageField(blank=True, null=True, help_text='The picture shoulde be at least 512px by 512px and either .jpg or .png')
    name_of_md = models.CharField(max_length=255)
    position = models.CharField(max_length=50)
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'MDs Message'


class AboutUs(models.Model):
    description = RichTextField()
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')

    class Meta:
        verbose_name_plural = 'About Us'



class Mission(models.Model):
    title = models.CharField(max_length=200)
    statement = RichTextField()
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Mission Statement'

