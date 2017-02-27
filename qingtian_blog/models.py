# coding: utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 100)
	blog_tag = models.CharField(max_length=20, default="hello")
	# blog_type 只有C#b, python, webFront, linux,datastruct四种选择
	blog_type = models.CharField(max_length = 20, choices=[
		('C#', 'C#小记'),
		('python', 'python'),
		('webFront', '前端'),
		('linux', 'linux'),
		('datastruct','数据结构')])
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
		verbose_name_plural = '博客' # 显式指定管理站点的显示，

class UploadFile(models.Model):
	HtmlFile = models.FileField(upload_to='templates/', max_length = 100)
	title = models.CharField(max_length=50, default='updloadfile')
	class Meta:
		verbose_name='html文件'
		verbose_name_plural = 'HTML文件'
	def __unicode__(self):
		return self.title
		pass
blogtype = {
	'C#': 'C#',
	'python': 'python',
	'webFront': 'webFront',
	'linux': 'linux',
	'datastruct': 'datastruct'
}

