from django.contrib import admin
from .models import BaseModel, Fossil

# Register your models here.
admin.site.register(BaseModel)
admin.site.register(Fossil)
