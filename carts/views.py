from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *


def cart_page(request):
    if not request.user.is_authenticated:
        return redirect('account:login_page')
    else:
        return redirect('home_page')




def addOrder_page(request,product_id):
    if not request.user.is_authenticated:
        return redirect('account:login_page')

    if request.method == "GET":
        cart = Cart.objects.filter(owner=request.user,is_paid=False).first()
        if cart is None:
            cart_create = Cart.objects.create(owner=request.user,is_paid=False)

        try:
            product = Product.objects.filter(id=product_id).first()

            physical_check = cart.physical_set.filter(product_id=product_id).first()
            digital_check = cart.digital_set.filter(product_id=product_id).first()

            if physical_check is not None or digital_check is not None:
                return JsonResponse({'status': 'False'})

            if product.price == 0:
                product.price = 'رایگان'

            if product.digital_or_physical == True:
                cart.physical_set.create(product_id=product.id,price=product.price)
                return JsonResponse({'status': 'True'})
            else:
                cart.digital_set.create(product_id=product.id,price=product.price)
                return JsonResponse({'status': 'True'})

        except: return redirect('home_page')

    else: return redirect('product:products_page')


def deleteOrder_page(request,product_id):
    if not request.user.is_authenticated:
        return redirect('account:login_page')

    if request.method == "GET":
        cart = Cart.objects.filter(owner=request.user,is_paid=False).first()
        if cart is not None:

            try:
                product = Product.objects.filter(id=product_id).first()
                if product.digital_or_physical == True:
                    order = Physical.objects.filter(product_id=product_id).first()
                    order.delete()
                else:
                    order = Digital.objects.filter(product_id=product_id).first()
                    order.delete()

            except: return redirect('home_page')

    else: return redirect('home_page')