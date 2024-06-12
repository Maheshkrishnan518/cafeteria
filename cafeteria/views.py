from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect  
from cafeteria.forms import CafeteriaForm  
from cafeteria.models import Cafeteria 
import os
from django.contrib import messages
from django.http import HttpResponse
import datetime
# Create your views here.
from .models import *
# Create your views here.  
def caf(request):  
    if request.method == "POST":  
        form = CafeteriaForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save() 
                img_object = form.instance 
                return redirect('/ad_manage_menu',{'img_obj': img_object})  
            except:  
                pass  
    else:  
        form = CafeteriaForm()  
    return render(request,'index.html',{'form':form})  
 
def edit(request, id):  
    cafeteria = Cafeteria.objects.get(id=id)  
    return render(request,'edit.html', {'cafeteria':cafeteria})  

def update(request, id):  
    cafeteria = Cafeteria.objects.get(id=id)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(cafeteria.image_item) > 0:
                os.remove(cafeteria.image_item.path)
            cafeteria.image_item = request.FILES['image_item']
        cafeteria.item_name = request.POST.get('item_name')
        cafeteria.amount = request.POST.get('amount')
        cafeteria.description = request.POST.get('description')
        cafeteria.type = request.POST.get('type')
        cafeteria.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/ad_manage_menu')

    context = {'cafeteria':cafeteria}
    return render(request, 'edit/'+cafeteria.id, context)


def destroy(request, id):  
    cafeteria = Cafeteria.objects.get(id=id) 
    cafeteria.delete()  
    return redirect("/ad_manage_menu")  


def index(request):
    datas=c_rt.objects.all()
    l=[]
    for i in datas:
        l.append(i.item_details)
    count=datas.count()
    data = Cafeteria.objects.all()
    return render(request,'index1.html',{'data':data,'datas':datas,'count':count,'item':l})

def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'Contact.html')
def order(request):
    return render(request,'order.html')

def additem(request):
    return render(request,'add.html')
def demiadd_items(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        # stock = request.POST['stock']
        discription = request.POST['discription']
        image = request.FILES['image']
        data = Cafeteria.objects.create(item_name=name,amount=price,description=discription,image_item=image)
        data.save()
        return redirect(demiadd_items)
    else:
        return render(request,'add.html')
def car(request,d):
        p_de=Cafeteria.objects.get(pk=d)
        datas=c_rt.objects.create(item_details=p_de,price=0,tprice=0)
        datas.save()
        return redirect(index)

def viewcart(request):
    datas=c_rt.objects.all()
    sub={}
    total=0
    su=datas
    for i in su:
        sub[i.item_details]=[i.quantity,i.pk,i.item_details.amount*i.quantity]
    print(sub)
    for i in datas:
        total=total+i.item_details.amount * i.quantity
    return render(request,'viewcart.html',{'datas':datas,'cl':sub,'total':total})

def minuscart(d2,de):
    c=c_rt.objects.get(id=de)
    if c.quantity>1:
        c.quantity = c.quantity - 1
        c.save()
    else:
        c.delete()
    return redirect(viewcart)

def pluscart(d3,de):
    c=c_rt.objects.get(id=de)
    c.quantity = c.quantity + 1
    c.save()
    return redirect(viewcart)
def del_cart(request,d):
    datas=c_rt.objects.get(pk=d)
    datas.delete()
    return redirect(viewcart)

def placeorder(r):
    datas=c_rt.objects.all()
    for item in datas:
        ordernow.objects.create(
        name = item.item_details.item_name,
        price = item.item_details.amount,
        quantity = item.quantity,
        totalprice= item.item_details.amount * item.quantity
                    )
    datas.delete()
    return redirect(index)

def myorders(request):
    datas=ordernow.objects.all()
    return render(request,'myorders.html',{'datas':datas})

def ad_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        try:
            if username=='admin@gmail.com' and password=='admin':
                request.session['admin']=username
                return redirect(admin)
        except:
            messages.add_message(request, messages.INFO, "Admin Not Login")
    return render(request,'admin-login.html') 

def admin(request):
    if 'admin' in request.session:
        return render(request,'ad_home.html')
def ad_menu(request):
      datas=Cafeteria.objects.all
      return render(request,'ad_manage-menu.html',{'datas':datas}) 
def ad_view_orders(request):
        datas=ordernow.objects.all()
        return render(request,'ad_view_orders.html',{'datas':datas}) 

def ad_reviews(request):
        return render(request,'ad_review.html') 
def ad_add(request):
        return render(request,'ad_addproducts.html') 
def ad_logout(request):
    if 'admin' in request.session:
        request.session.flush()
        return redirect(ad_login)