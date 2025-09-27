
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/', views.add,name='add'), 
    path('add_task/',views.add_tasks,name='add_task'),
    path('delete/', views.delete,name='delete'), 
    path('delete_member/<int:id>',views.delete_member,name='delete_member'),   
    path('update_member/<int:id>',views.update_member,name='update_member'),
    # path('edit/',views.edit,name='edit')
]