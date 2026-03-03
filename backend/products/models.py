from django.db import models

# Create your models here.
class Product(models.Model):
   
    title=models.CharField(max_length=100 )
    price=models.DecimalField(max_digits=15,decimal_places=2,default=0.00)
    content=models.TextField(null=True,blank=True)
    def __str__(self):
            return self.title