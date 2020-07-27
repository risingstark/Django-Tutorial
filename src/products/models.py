from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=5,decimal_places=2)
    summary     = models.TextField(blank=True, null=False)
    etc         = models.TextField(null=False)
    feature     = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"/products/{self.id}/"