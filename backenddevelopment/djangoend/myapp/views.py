from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name':'Patrick',
        'age':34,
        'nationality':'Kenyan'
    }
    return render(request,'index.html',  context)


def visitors(request):
    return render(request,'visitors.html')


def counter(request):
    text=request.GET['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'words':amount_of_words})