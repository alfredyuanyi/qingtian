from django.conf.urls import url
from qingtian_blog import views

urlpatterns = [
	url(r'CSharpbaseblog/$', views.CSharpBase, {'blog_type': 'C#base'})
]