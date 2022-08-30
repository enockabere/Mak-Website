from operator import truediv
from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from blog.models import STATUS

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Frequently Asked Question'

    @property
    def short_description(self):
        return truncatechars(self.answer, 30)

    def __str__(self):
        return self.question


class PubCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
class Publication(models.Model):

    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='media')
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PubCategory, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = 'Resource'


    def __str__(self):
        return self.name


class Privacy(models.Model):
    title = models.CharField(max_length=200, default='Privacy Policy')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='media')
    status = models.IntegerField(choices=STATUS, default=0, help_text='change to published to be seen')

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policy'


    def __str__(self):
        return self.title

class Terms(models.Model):
    title = models.CharField(max_length=200, default='Terms of Service')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='media')
    status = models.IntegerField(choices=STATUS, default=0, help_text='change to published to be seen')

    class Meta:
        verbose_name = 'Terms of Service'
        verbose_name_plural = 'Terms of Service'


    def __str__(self):
        return self.title