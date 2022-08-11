from math import trunc
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db import models
from blog.models import STATUS

# Create your models here.

CATEGORY = [
    (0, 'Board of management'),
    (1, "Leadership")
]


class Personel(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(
        max_length=50, blank=True, help_text='Optional')
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media',  null=True,
                              blank=True, help_text='Image size should be in .jpg or .png')
    category = models.IntegerField(
        choices=CATEGORY, default=0, help_text='select Peronel membership title')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Personel'
        verbose_name_plural = 'Personel'

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def full_name(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    full_name.short_description = 'Name'
    full_name.allow_tags = True

    def profile_photo(self):
        return mark_safe('<img src="{}" width="100px" />'.format(self.image.url))

    profile_photo.short_description = 'Image'
    profile_photo.allow_tags = True

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)


class MDsMessage(models.Model):
    title = models.CharField(max_length=200, help_text="e.g. John's Message")
    message = models.TextField()
    image = models.ImageField(
        blank=True, help_text='The profile picture shoulde be at least 512px by 512px and either .jpg or .png')
    name_of_md = models.CharField(
        max_length=255, help_text='Write the full name')
    position = models.CharField(max_length=50)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'MDs Message'

    @property
    def short_description(self):
        return truncatechars(self.message, 50)

    def profile_photo(self):
        return mark_safe('<img src="{}" width="100px" />'.format(self.image.url))

    profile_photo.short_description = 'Image'
    profile_photo.allow_tags = True

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    description = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name_plural = 'About Us'


    @property
    def short_description(self):
        return truncatechars(self.description, 50)

    def __str__(self):
        return self.short_description


class Mission(models.Model):
    title = models.CharField(max_length=200)
    statement = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Mission Statement'


class Department(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    @property
    def short_content(self):
        return truncatechars(self.content, 30)

    def __str__(self):
        return self.title