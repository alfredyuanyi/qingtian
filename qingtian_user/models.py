# coding: utf8
from __future__ import unicode_literals

from django.db import models

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
	pass
