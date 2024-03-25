from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', include('marketplace.urls')),
    path('admin/', admin.site.urls), 
   path('categories/', views.categories, name='categories'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('category_items/<str:category>/', views.category_items, name='category_items'),

]
