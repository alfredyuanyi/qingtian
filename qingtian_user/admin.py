from django.contrib import admin
from qingtian_user.models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'password')
	list_filter = ('username',)
	ordering = ('username',)
	pass
class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'blog', 'datetime')
	list_filter = ('datetime','blog')
	ordering = ('datetime',)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)