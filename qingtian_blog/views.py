# coding:utf8
from django.shortcuts import render
from qingtian_blog.models import *
# Create your views here.
def Home(request):
	return render(request, template_name = 'home.html')
	pass
def CSharpBase(request, blog_type):
	blogs = Blog.objects.filter(blog_type = blog_type)
	return render(request, 
		template_name = 'C#base.html',
		context = {'blogs': blogs})
	pass