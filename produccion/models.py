from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    product_key = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    price = models.FloatField()
    delete = models.BooleanField()

    class Meta:
        db_table='productos'

    def __str__(self):
        return self.product_key
