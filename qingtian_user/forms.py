# coding: utf8
from django import forms
from qingtian_user.models import User, Comment
from qingtian_blog.models import Blog
class UserForm(forms.Form):
	username = forms.CharField(max_length = 30, required = True, label = '用户名')
	password = forms.CharField(max_length = 25, required = True, label = '密码', widget = forms.PasswordInput)
	checkpassword = forms.CharField(max_length = 25, required = True, label = '确认密码', widget = forms.PasswordInput)
	email = forms.EmailField(required = True, label = '邮箱', widget = forms.EmailInput)
	def clean_checkpassword(self):
		checkpassword = self.cleaned_data['checkpassword']
		password = self.cleaned_data['password']
		if checkpassword != password:
			raise forms.ValidationError("密码不一致，请确认后重新输入")
			pass
		return  checkpassword
		pass
	pass

class LoginForm(forms.Form):
    # TODO: Define form fields here
    username = forms.CharField(max_length = 30, required = True, label = '用户名')
    password = forms.CharField(max_length = 25, required = True, label = '密码', widget = forms.PasswordInput)
    # def clean_username(self):
    # 	print self.cleaned_data
    # 	username = self.cleaned_data['username']
    # 	try:
    # 		user = User.objects.get(username = username)
    # 		pass
    # 	except User.DoesNotExist:
    # 		raise forms.ValidationError('不存在该用户，请确认用户名后再重新输入')
    # 	return username
    # 	pass
    def clean_password(self):
    	username = self.cleaned_data['username']
    	password = self.cleaned_data['password']
    	try:
    		user = User.objects.get(username = username)
    		pass
    	except User.DoesNotExist:
    		raise forms.ValidationError('不存在该用户，请确认用户名后再重新输入')
    	if password != User.objects.get(username = username).password:
    		raise forms.ValidationError('密码错误，请确认后重新输入')
    		pass
    	return password
    	pass
    pass

class CommentForm(forms.Form):
	username = forms.CharField(max_length = 30)
	blog = forms.CharField()
	content = forms.CharField()
	def clean_username(self):
		try:
			user = User.objects.get(username = self.cleaned_data['username'])
			pass
		except User.DoesNotExist:
			raise forms.ValidationError('不存在该用户')
		return user
		pass
	def clean_blog(self):
		try:
			blog = Blog.objects.get(id = int(self.cleaned_data['blog']))
			pass
		except Blog.DoesNotExist:
			raise forms.ValidationError('不存在该博客！')
		return blog
		pass
	def clean_content(self):
		return self.cleaned_data['content']
		pass
	pass

