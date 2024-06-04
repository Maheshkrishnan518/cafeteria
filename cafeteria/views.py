from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect  
from cafeteria.forms import CafeteriaForm  
from cafeteria.models import Cafeteria 
import os
from django.contrib import messages
# Create your views here.  
def caf(request):  
    if request.method == "POST":  
        form = CafeteriaForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save() 
                img_object = form.instance 
                return redirect('/show',{'img_obj': img_object})  
            except:  
                pass  
    else:  
        form = CafeteriaForm()  
    return render(request,'index.html',{'form':form})  
def home(request):
    cafeteria = Cafeteria.objects.all()  
    return render(request,"home.html",{'cafeteria':cafeteria}) 
def show(request):
    cafeteria = Cafeteria.objects.all()  
    return render(request,"show.html",{'cafeteria':cafeteria})  
def edit(request, id):  
    cafeteria = Cafeteria.objects.get(id=id)  
    return render(request,'edit.html', {'cafeteria':cafeteria})  
def update(request, id):  
    """
    cafeteria = Cafeteria.objects.get(id=id)  
    form = CafeteriaForm(request.POST,request.FILES, instance = cafeteria)  
    if form.is_valid():  
        form.save()
        return redirect("/show")  
    return render(request, 'edit.html', {'cafeteria': cafeteria})  
    """
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
        return redirect('/show')

    context = {'cafeteria':cafeteria}
    return render(request, 'edit/'+cafeteria.id, context)


def destroy(request, id):  
    cafeteria = Cafeteria.objects.get(id=id) 
    cafeteria.delete()  
    return redirect("/show")  