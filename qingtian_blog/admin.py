# coding: utf8
from django.contrib import admin
from qingtian_blog.models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'blog_tag','traffic', 'approval', 'oppostion')
	search_fields = ('date', 'title', 'blog_tag', 'blog_type')
	list_filter = ('blog_type', 'date')
	ordering = ('-blog_tag',)
	pass
class UploadFileAdmin(admin.ModelAdmin):
	admin.site.register(UploadFile)

admin.site.register(Blog, BlogAdmin)








