from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', include('marketplace.urls')),
    path('admin/', admin.site.urls), ]