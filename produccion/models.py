from django.db import models
import uuid 

class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    product_key = models.CharField(max_length=255)
    notes = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.product_key

class Production(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    id = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  
    
    class Meta:
        db_table = 'produccion'

    def __str__(self):
        return self.id