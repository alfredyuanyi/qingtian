# coding: utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	blog_type = models.CharField(max_length = 20)
	date = models.DateField()
	traffic = models.IntegerField(default = 0)
	approval = models.IntegerField(default = 0)
	oppostion = models.IntegerField(default = 0)
	def __unicode__(self):
		return self.title
		pass
	class Meta:
		ordering = ['-traffic']
		verbose_name = '博客'
