# coding:utf8
from django.shortcuts import render, redirect
from django.http import Http404,HttpResponse
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth import authenticate, login, logout
from qingtian_user.models import *
from qingtian_user.forms import *
# Create your views here.
def Register(request):
	if request.method == 'POST':
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
			form = UserForm(request.POST)
			if form.is_valid():
				form_data = form.cleaned_data
				user = User.objects.create(username = form_data['username'],
					password = form_data['password'],
					email = form_data['email'])
				user.save()
				authUser = AuthUser.objects.create_user(username = user.username, password = user.password)
				authUser.save()
				loginUser = authenticate(username = user.username, password = user.password)
				if loginUser is not None:
					login(request, user = loginUser)
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
