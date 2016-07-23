# coding: utf8
from django import forms

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

