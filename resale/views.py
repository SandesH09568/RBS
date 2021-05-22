from django.shortcuts import render
from django.conf import settings
# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def contact(request):
    return render(request,'contact.html')
def detailproduct(request):
    return render(request,'detail-product.html')


def faq(request):
    return render(request,'faq.html')
def privacy(request):
    return render(request,'privacy.html')
def setting(request):
    return render(request,'setting.html')
def shop(request):
    return render(request,'shop.html')
def terms(request):
    return render(request,'terms.html')
def transaction(request):
    return render(request,'transaction.html')
