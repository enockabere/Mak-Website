from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from blog.models import STATUS
# Create your models here.


class JobAdvert(models.Model):
    POSITION_TYPE = [
        (0, 'Full Time'),
        (1, 'Part Time'),
        (2, 'Internship'),
        (3, 'Attachment')
    ]

    title = models.CharField(max_length=200)
    job_ID = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    job_description = models.TextField()
    resposibilities = models.TextField()
    qualification = models.TextField()
    advert_file = models.FileField(upload_to='media', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, help_text='Date Published')
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')
    job_type = models.IntegerField(choices=POSITION_TYPE, default=0,help_text = 'Choose the appropriate job type to advertise')


    class Meta:
        verbose_name = 'Job Advert'

    @property
    def short_description(self):
         return truncatechars(self.job_description, 50)

    def __str__(self):
        return self.title

class Tender(models.Model):
    TENDER_STATUS = [
        ('open', 'open'),
        ('closed', 'closed')
    ]
    title = models.CharField(max_length=200)
    ref_number = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='media')
    pub_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    tender_status = models.CharField(choices=TENDER_STATUS, max_length=20, default='open')
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')


    class Meta:
        ordering = ['-pub_date']

    @property
    def short_description(self):
        return truncatechars(self.description, 30)

    def __str__(self):
        return self.title
