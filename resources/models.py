from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
        