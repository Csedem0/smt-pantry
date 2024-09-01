from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
]
