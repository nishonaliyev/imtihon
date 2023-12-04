from django.contrib import admin
from .models import Fan, Savollar


admin.site.register(Fan)
admin.site.register(Savollar)

class Fanadmin(admin.ModelAdmin):
    list_display = ['fan_nomi', 'imthon_joyi', 'oqituvchi']

class Savoladmin(admin.ModelAdmin):
    list_display = ['savol', 'fan']

