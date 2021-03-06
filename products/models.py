from django.db import models

# Create your models here.
class Product(models.Model):
    def __repr__(self):
        return '{} {}'.format(self.title, self.id).title()

    title = models.CharField(max_length=120) # must define a max length
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()
    featured = models.BooleanField(default=False)
