from django.db import models

# Create your models here.
from django.db import models  
class Cafeteria(models.Model):
    item_name = models.CharField(max_length=30)  
    amount = models.IntegerField() 
    image_item = models.ImageField(upload_to='images')   
    description = models.CharField(max_length=200)  
    type=models.CharField(max_length=50)  
    class Meta:  
        db_table = "cafeteria"  

class add_items(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    discription = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class ordernow(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    quantity = models.IntegerField()
    totalprice = models.IntegerField()

    def __str__(self):
        return self.name
class c_rt(models.Model):
    item_details=models.ForeignKey(Cafeteria,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    tprice=models.IntegerField()
    delivered=models.BooleanField(default=False)
