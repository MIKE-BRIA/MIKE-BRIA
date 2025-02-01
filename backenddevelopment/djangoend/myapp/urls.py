from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('<str:pk>', views.profile,name='profile'),
    path('visitors',views.visitors,name='visitors'),
    path('counter',views.counter,name='counter')
]
