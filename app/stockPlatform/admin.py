from django.contrib import admin
from .models import CustomUser, StockDetail


# Register your models here.

admin.site.register(StockDetail)
admin.site.register(CustomUser)
