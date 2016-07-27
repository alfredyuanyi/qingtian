# coding:utf8
from django.shortcuts import render, redirect
from django.http import Http404,HttpResponse
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from qingtian_user.models import *
from qingtian_user.forms import *
# Create your views here.
@csrf_exempt
def TestUsername(request):
	if request.method == 'POST':
		username = request.POST['username']
		try:
			user = User.objects.get(username = username)
			return HttpResponse('该用户名已存在，请重新输入')
			pass
		except User.DoesNotExist:
			return HttpResponse('用户名可用')
		pass
	pass
def Register(request):
	if request.method == 'POST':
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
			form = UserForm(request.POST)
			if form.is_valid():
				form_data = form.cleaned_data
				if User.objects.get(username = form_data['username']) is not None:
					return HttpResponse('该用户名已存在，请重新输入')
					pass
				user = User.objects.create(username = form_data['username'],
					password = form_data['password'],
					email = form_data['email'])
				authUser = AuthUser.objects.create_user(username = user.username, password = user.password)
				authUser.save()
				loginUser = authenticate(username = user.username, password = user.password)
				if loginUser is not None:
					login(request, user = loginUser)
					user.save()
					return redirect('/home/')
					pass
				pass
			pass
		else:
			return HttpResponse("请允许设置cookie后再试一遍。")
		pass
	else:
		form = UserForm(initial = {'username': '请输入用户名',
			'email': '请输入可以联系到您邮箱地址'})
		pass
	request.session.set_test_cookie()
	return render(request, 
		template_name = 'userform.html',
		context = {'form': form})
	pass

def Logout(request):
	user = request.user
	logout(request)
	AuthUser.objects.filter(username = user.username).delete()
	return redirect('/users/loginservice/')
	pass

def Login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			authUser = AuthUser.objects.create_user(username = data['username'], password= data['password'])
			authUser.save()
			loginUser = authenticate(username = data['username'], password = data['password'])
			if loginUser is not None:
				login(request, user = loginUser)
				return redirect('/home/')
				pass
			pass
		pass
	else:
		form = LoginForm(initial = {
			'username': '请输入用户名',
			'password': '请输入密码'
			})
		pass
	return render(request, 
		template_name = 'login.html',
		context = {'form': form})
	pass

def SetComment(request, blogid, blog_type):
	if request.method == 'POST':
		if request.user.is_authenticated():
			form = CommentForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				comment = Comment.objects.create(content = data['content'],
					user = data['username'],
					blog = data['blog'])
				comment.save()
				return HttpResponse('评论成功，感谢您的评论！')
				pass
			pass
		else:
			return HttpResponse('请先登陆，登陆后才可评论')
		pass
	else:
		return HttpResponse('请求方法错误！请摆好姿势')
	pass
@csrf_exempt
def TestLogin(request):
	if request.user.is_authenticated():
		return HttpResponse('')
		pass
	else:
		return HttpResponse('请先登陆，登陆后才可评论')
	pass