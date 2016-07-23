# coding: utf8
from django.contrib import admin
from qingtian_blog.models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'traffic', 'approval', 'oppostion')
	search_fields = ('date', 'title', 'content', 'blog_type')
	list_filter = ('blog_type', 'date')
	ordering = ('-traffic',)
	pass


admin.site.register(Blog, BlogAdmin)
