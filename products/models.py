from django.db import models

# Create your models here.
class Product(models.Model):
    num_of_shift = models.IntegerField() #max_length required
    num_of_defective_parts = models.IntegerField(blank=True, null=True)
    description = models.TextField(default='Please Specify the reason why this item is defective')
