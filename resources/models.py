from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = RichTextField(null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question


class Publication(models.Model):

    PUB_CATEGORY = [

        (0, 'default'),
        (1, 'advertisement')
    ]

    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='media')
    category = models.IntegerField(choices=PUB_CATEGORY, default=0)

    def __str__(self):
        return self.name


class JobAdvert(models.Model):
    title = models.CharField(max_length=200)
    job_ID = models.CharField(max_length=50)
    job_description = RichTextField()
    resposibilities = RichTextField()
    qualification = RichTextField()
    advert_file = models.FileField(upload_to='media')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

