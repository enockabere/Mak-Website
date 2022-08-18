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


class Publication(models.Model):

    PUB_CATEGORY = [

        (0, 'Default'),
        (1, 'Advertisement')
    ]

    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='media')
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=PUB_CATEGORY, default=0)
    status = models.IntegerField(choices=STATUS, default=0)


    def __str__(self):
        return self.name

