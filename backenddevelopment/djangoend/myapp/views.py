from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name='Everywhere'
    feature1.details='Our service is very quick and reliable throughout the country and even worldwide'
    
    feature2 = Feature()
    feature2.id=1
    feature2.name = 'Good Quality'
    feature2.details = 'We Make sure the quality of your products arrive in their destination without any interference'
    
    feature3 = Feature()
    feature3.id=2
    feature3.name='Good Customer Care'
    feature3.details='We respond to our customers need quickly and we have the best rated customer care service within the industry'
    
    features = [feature1,feature2,feature3]
    return render(request,'index.html', {'features':features} )


def about(request):
    return render(request,'about.html')


def visitors(request):
    return render(request,'visitors.html')


def counter(request):
    text=request.POST['text']
    amount_of_words=len(text.split())
    return render(request,'counter.html',{'words':amount_of_words})