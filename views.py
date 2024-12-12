from django.shortcuts import render,redirect,HttpResponseRedirect
import random
from django.contrib.auth.models import User
from .models import PlantCategory, Plant,CartItems
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView,CreateView,TemplateView
from django.contrib.auth import authenticate,login,logout
from.forms import Regform
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
def home(request):
    cata=PlantCategory.objects.all()
    context={'cata':cata}
    return render(request,'home.html',context)
def register(request):
    form=Regform()
    if request.method=='POST':
        form=Regform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You are logged in')
            return redirect(home)
    else:
        form=Regform()
    return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method=='POST':
        usernam=request.POST['username']
        paswd=request.POST['password']
        user=authenticate(request,username=usernam,password=paswd)
        if user:
            login(request,user)
            messages.success(request,'user has been logged in')
            return redirect(home)
        else:
            messages.error(request,'invalid login')
    return render(request,'login.html')
def logoutpage(request):
    logout(request)
    return redirect(home)


def catz(request):
    ca=PlantCategory.objects.all()
    return render(request,'cate.html',{'ca':ca})
def details(request,name):
    a=Plant.objects.get(name=name)
    return render(request,'detail.html',{'a':a})
def catlist(request,name):
    pr=Plant.objects.filter(name=name)
    return render(request,'list.html',{'pr':pr})
def add_to_cart(request, id):
    plant = Plant.objects.get(pk=id)
    cart = request.session.get('cart', [])
    cart.append({'id': plant.id, 'name': plant.name, 'price': float(plant.price)})
    request.session['cart'] = cart
    return redirect('plant_list')

def view_cart(request):
    cart = request.session.get('cart', [])
    total_price = sum(item['price'] for item in cart)
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['id'] != id]
    request.session['cart'] = cart
    return redirect('view_cart')
def payment(request,id):
    pay=Plant.objects.filter(pk=id)
    return render(request,'payment.html',{'pay':pay})
def payment_successful(request,):
 
    return render(request,'sucessfull.html')
def items(request):
  search_items=request.GET['search_items']
  get=Plant.objects.filter(name__icontains=search_items)
  return render(request,'items.html',{'get':get})

def abpro(request):
    return render(request,'about.html')  
class add_categories(CreateView):
    model=PlantCategory  
    fields='__all__'
    context_object_name='form'
    success_url='home'
    template_name='add_Cate.html'

