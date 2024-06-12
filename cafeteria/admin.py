from django.contrib import admin

# Register your models here.
from .models import Cafeteria
from .models import add_items
from .models import ordernow
from .models import c_rt
# Register your models here.
admin.site.register(add_items)
admin.site.register(ordernow)
admin.site.register(c_rt)
admin.site.register(Cafeteria)