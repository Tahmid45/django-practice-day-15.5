from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_album, name = 'addAlbum'),
    path('edit/<int:id>', views.edit_album, name = 'editAlbum'),
    path('delete/<int:id>', views.delete_album, name = 'deleteAlbum'),
]
