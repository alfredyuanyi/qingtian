from django.contrib import admin
from qingtian_user.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'password')
	list_filter = ('username')
	ordering = ('username')
	pass

admin.site.register(User, UserAdmin)