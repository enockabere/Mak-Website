from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db import models
from blog.models import STATUS


class PhotoGallery(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    caption = models.TextField()

    @property
    def short_description(self):
        return truncatechars(self.caption, 20)

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'Image'
    photo.allow_tags = True

    def __str__(self):
        return self.title


class VideoGallery(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField()
    caption = models.TextField()

    @property
    def short_description(self):
        return truncatechars(self.caption, 20)

    def vid(self):
        return mark_safe('<video src="{}" width="150px"></video>'.format(self.video.url))

    vid.short_description = 'Video'
    vid.allow_tags = True

    def __str__(self):
        return self.title
