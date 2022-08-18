from django.db import models
from blog.models import STATUS

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default = 0, help_text = 'change to published for the data to appear')

    def __str__(self):
        return self.title

