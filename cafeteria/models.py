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
