from django.db import models

# Create your models here.
class Article(models.Model):

    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    feature     = models.BooleanField(default=False)

