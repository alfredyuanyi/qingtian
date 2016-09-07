# coding:utf8
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from qingtian_blog.models import *
from qingtian_user.models import Comment
# Create your views here.
def Home(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			return render(request, 
				template_name = 'home.html',
				context = {'haslogin': True})
			pass
		else:
			return render(request, 
			template_name = 'home.html',
			context = {'haslogin': False})
		pass
	else:
		return Http404
	pass
def BlogType(request, blog_type):
	if request.method == 'GET':
		blogs = Blog.objects.filter(blog_type = blog_type)
		Btype = blogtype[blog_type]
		if request.user.is_authenticated():
			return render(request, 
				template_name = 'blogtype.html',
				context = {'blogs': blogs,
				'blog_type': Btype,
				'haslogin': True})
			pass
		else:
			return render(request, 
			template_name = 'blogtype.html',
			context = {'blogs': blogs,
			'blog_type': Btype,
			'haslogin': False})
		pass
	else:
		return Http404
	pass
def Blogid(request, blogid, blog_type):
	if request.method == 'GET':
		try:
			blog = Blog.objects.get(id = blogid)
			pass
		except Blog.DoesNotExist:
			return Http404
		Btype = blogtype[blog_type]
		blog.traffic += 1
		blog.save()
		comment = blog.comment_set.all()
		if request.user.is_authenticated():
			return render(request,
				template_name = blog.blog_tag + '.html',
				context = {'blog': blog,
				'blog_type': Btype,
				'haslogin': True,
				'comments': comment})
			pass
		return render(request,
			template_name = blog.blog_tag + '.html',
			context = {'blog': blog,
			'blog_type': Btype,
			'haslogin': False,
			'comments': comment})
		pass
	else:
		return Http404
	pass

def Contact(request):
	if request.method == 'GET':
		if request.user.is_authenticated():
			return render(request, 
				template_name = 'contact.html',
				context = {'haslogin': True})
			pass
		else:
			return render(request, 
			template_name = 'contact.html',
			context = {'haslogin': False})
		pass
	else:
		return Http404
	pass
