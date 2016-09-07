# coding: utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 100)
	blog_tag = models.CharField(max_length=20, default="hello")
	# blog_type 只有C#base, C#advance, Bootstrap, ubuntu四种选择
	blog_type = models.CharField(max_length = 20, choices=[
		('C#base', 'C#base'),
		('C#advance', 'C#advance'),
		('Bootstrap', 'Bootstrap'),
		('ubuntu', 'ubuntu')])
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
	
	class Meta:
		verbose_name='html文件'
		verbose_name_plural = 'HTML文件'
blogtype = {
	'C#base': 'C#基础',
	'C#advance': 'C#进阶',
	'Bootstrap': 'Bootstrap',
	'ubuntu': 'ubuntu'
}

