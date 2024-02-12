from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.HomePage,name='HomePage'),
    path('result/', views.sum,name='sum'),

]
    
