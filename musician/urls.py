from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_musician, name = 'addMusician'),
    path('edit/<int:id>', views.edit_musician, name = 'editMusician'),
    # path('delete/<int:id>', views.delete_musician, name = 'deleteMusician'),
]
