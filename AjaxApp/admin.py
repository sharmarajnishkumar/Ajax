from django.contrib import admin
from .models import User

# Register your models here.
# @admin.register(User)
# class AdminUser(admin.ModelAdmin):
#     list_display = ('name','emai','mobile','city')
admin.site.register(User)