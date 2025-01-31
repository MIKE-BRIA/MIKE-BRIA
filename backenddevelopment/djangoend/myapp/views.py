from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    
    return render(request,'index.html', {'features':features} )


def about(request):
    return render(request,'about.html')


def visitors(request):
    return render(request,'visitors.html')


def counter(request):
    text=request.POST['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'words':amount_of_words})