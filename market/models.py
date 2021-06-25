from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Stock(models.Model):
    video_link = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('stock-pk-slug-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
