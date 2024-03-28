from django.urls import path, include
from django.contrib import admin
from marketplace import views

from django.urls import path, re_path




urlpatterns = [
    path('', include('marketplace.urls')),
    path('admin/', admin.site.urls), 
   path('categories/', views.categories, name='categories'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('category_items/<str:category>/', views.category_items, name='category_items'),
    path('item/<str:id>/', views.item_detail, name='item_detail'),
    re_path(r'^item/$', views.item, name='item'),
    
]
