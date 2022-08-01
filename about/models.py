from django.db import models

# Create your models here.


class Personel(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True, help_text='Optional')
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.middle_name, self.last_name)

