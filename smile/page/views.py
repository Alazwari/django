from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'page/index.html')

def contact(request):
    return render(request, 'page/contact.html')