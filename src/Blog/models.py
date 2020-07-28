from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):

    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    feature     = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("Blog:article-detail", kwargs={"id": self.id})
        # hard coding version of dynamic URL
        # f"/products/{self.id}/"s