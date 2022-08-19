from django.db import models

# Create your models here.


class Feedback(models.Model):
    type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

