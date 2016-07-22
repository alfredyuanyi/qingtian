from django.conf.urls import url
from qingtian_blog import views

urlpatterns = [
	url(r'CSharpbaseblog/$', views.BlogType, {'blog_type': 'C#base'}),
	url(r'CSharpbaseblog/(?P<blogid>\d*)/$', views.Blogid, {'blog_type': 'C#base'}),
	url(r'CSharpadvanceblog/$', views.BlogType, {'blog_type': 'C#advance'}),
	url(r'CSharpadvanceblog/(?P<blogid>\d*)/$', views.Blogid, {'blog_type': 'C#advance'}),
	url(r'Bootstrapblog/$', views.BlogType, {'blog_type': 'Bootstrap'}),
	url(r'Bootsrapblog/(?P<blogid>\d*)/$', views.Blogid, {'blog_type': 'Bootstrap'}),
	url(r'ubuntublog/$', views.BlogType, {'blog_type': 'ubuntu'}),
	url(r'ubuntublog/(?P<blogid>\d*)/$', views.Blogid, {'blog_type': 'ubuntu'}),
]