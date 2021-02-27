from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    catalogue_num = models.IntegerField(default=5) #default is what is registered as value if no other value is received
    name = models.CharField(max_length=100, default='na') #string that has a max length of 100 characters
    date = models.CharField(max_length=100, default='na') #up to 100 characters, so it can give a description or range of dates
    #manufacturer = models.CharField(max_length=100)
    condition = models.TextField(default='na') #unrestricted text
    provenance = models.CharField(max_length=100, default='na') #the origin of item
    description = models.TextField(default='na') #unrestricted text
    item_type = models.CharField(max_length=100, default='na')
    staff_creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) #one to many relationship, a user can create many base models but 
    #a base model may only be created by 1 user. cascade on delete so the entry doesn't still exist in the users table.

    def __str__(self):
        return self.name

class Fossil(models.Model):
    base = models.ForeignKey(BaseModel, blank=True, null=True, on_delete=models.SET_NULL)
    size = models.IntegerField(blank=True, null=True) #allow field to be left blank and set to null 
    scientific_name = models.CharField(max_length=100, default='na') 

    def __str__(self):
        return self.base.name


