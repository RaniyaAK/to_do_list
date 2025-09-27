
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('add/', views.add,name='add'), 
    path('add_tasks/',views.add_tasks,name='add_tasks'),
    path('delete/<int:id>', views.delete,name='delete'), 
    path('delete_tasks/<int:id>',views.delete_tasks,name='delete_tasks'),   
    path('update_tasks/<int:id>',views.update_tasks,name='update_tasks'),
    # path('edit/',views.edit,name='edit')
]