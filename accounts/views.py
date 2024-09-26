from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from datetime import timedelta

@login_required
def home(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            # Calculate time difference between expiry date and current date
            time_difference = product.expiry_date - timezone.now().date()
            # If expiry date is within 3 days, send a notification
            if 0 < time_difference.days <= 3:
                messages.warning(request, f'Warning: {product.name} will expire in {time_difference.days} days!')
            messages.success(request, 'Product added successfully!')
            return redirect('home')
    else:
        form = ProductForm()
    
    pantry_products = Product.objects.all()
    for product in pantry_products:
        # Calculate days remaining for each product
        product.days_remaining = (product.expiry_date - timezone.now().date()).days
        # If product expires within 2 days, send a notification
        if product.days_remaining <= 2:
            messages.warning(request, f'Warning: {product.name} will expire in {product.days_remaining} days!')
    return render(request, 'index.html', {'form': form, 'pantry_products': pantry_products})


@login_required
def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('home')

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_details.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def share(request):
    return render(request, 'share.html')

def custom_logout(request):
    logout(request)
    return redirect('login')
