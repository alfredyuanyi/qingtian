# coding: utf8
from __future__ import unicode_literals

from django.db import models
from qingtian_blog.models import Blog
# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 30, blank = False, unique = True)
	password = models.CharField(max_length = 25, blank = False)
	email = models.EmailField()
	def __unicode__(self):
		return self.username
		pass
	class Meta:
		ordering = ['username']
		verbose_name = '用户'
		verbose_name_plural = '用户'
	pass
class Comment(models.Model):
	datetime = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(to = User)
	content = models.TextField()
	blog = models.ForeignKey(to = Blog)
	def __unicode__(self):
		return self.user.username + "'s comment to " + self.blog.title 
		pass
	class Meta:
		ordering = ['datetime']
		verbose_name = '评论'
		verbose_name_plural = '评论'
		pass
	pass