from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('visitors',views.visitors,name='visitors'),
    path('counter',views.counter,name='counter')
]
