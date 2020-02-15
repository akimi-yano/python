from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product_id_from_form = int(request.POST["product_id"])
    price_from_db = Product.objects.get(id=product_id_from_form).price
    total_charge = quantity_from_form * price_from_db
    new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    
    return redirect(f'/confirmation/{new_order.id}')

def confirm(request, id):
    new_order=Order.objects.get(id = id)
    total_spent=sum([o.total_price for o in Order.objects.all()])
    
    
    context={
        "order": new_order,
        "total_spent": total_spent
    }
    
    
    return render(request, "store/checkout.html", context)