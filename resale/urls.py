from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),


    path('shop/',views.shop,name="shop"),
    path('about/',views.about,name="about"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('contact/',views.contact,name="contact"),
    path('detail-product/',views.detailproduct,name="detail-product"),
    path('faq/',views.faq,name="faq"),
    path('privacy/',views.privacy,name="privacy"),
    path('setting/',views.setting,name="setting"),
    path('terms/',views.terms,name="terms"),
    path('transaction/',views.transaction,name="transaction"),

    

    
]