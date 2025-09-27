from django.db import models

# Create your models here.


class Table(models.Model):
  task= models.CharField(max_length=1000) 
  status= models.CharField(max_length=225) 
  actions = models.CharField(max_length=255) 
  created_date= models.DateField(auto_now_add=True)
  def __str__(self):
    return  self.task