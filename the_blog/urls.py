from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home, name = 'blog_Home'),
    path('about/', views.About, name = 'blog_About'),
    
]