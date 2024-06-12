"""crudexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static

from django.contrib import admin  
from django.urls import path  
from cafeteria import views  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('caf', views.caf),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),

    path('user',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('order',views.order),
    # path('orderednow/<int:a>',views.orderednow),
    path('additem',views.additem),
    path('demiadd_items',views.demiadd_items),
    path('add_to_cart/<int:d>',views.car),
    path('viewcart',views.viewcart),
    path('minuscart/<int:de>',views.minuscart),
    path('pluscart/<int:de>',views.pluscart),
    path('del_cart/<int:d>',views.del_cart),
    path('placeorder',views.placeorder),
    path('myorders',views.myorders),

    path('',views.ad_login),
    path('admin',views.admin),
    path('ad_manage_menu',views.ad_menu),
    path('ad_orders',views.ad_view_orders),
    path('ad_reviews',views.ad_reviews),
    path('ad_add',views.ad_add),
   path('ad_logout',views.ad_logout),
]  

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  