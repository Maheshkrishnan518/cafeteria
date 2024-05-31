from django.db import models  
from django.forms import fields    
from django import forms  

from cafeteria.models import Cafeteria 
class CafeteriaForm(forms.ModelForm):  
    class Meta:  
        model = Cafeteria 
        fields = "__all__"  