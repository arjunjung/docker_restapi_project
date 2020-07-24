from django.contrib import admin
from .models import ToyModel

class ToyModelAdmin(admin.ModelAdmin):
    list_display = ['name','category','price']

admin.site.register(ToyModel,ToyModelAdmin)
