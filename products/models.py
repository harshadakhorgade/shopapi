from django.db import models

# Create your models here.

class Category(models.Model):
    name =models.CharField( max_length=50 , unique =True)

    def __str__(self):
        return self.name


class Product(models.Model):
   name  =models.CharField(max_length=100)
   description = models.TextField()
   price = models.FloatField()
   stock = models.IntegerField()
   created_at= models.DateTimeField(auto_now_add =True)

   category = models.ForeignKey(Category , on_delete =models.CASCADE ,related_name="products")
   
   