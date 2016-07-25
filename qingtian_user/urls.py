from django.conf.urls import url
from qingtian_user import views
urlpatterns = [
	url(r'newuser/$', views.Register),
	url(r'loginservice/$', views.Login),
	url(r'logoutservice/$', views.Logout),
	url(r'newcomment/CSharpbaseblog/(?P<blogid>\d*)/$',views.SetComment, {'blog_type': 'C#base'}),
	url(r'newcomment/CSharpadvanceblog/(?P<blogid>\d*)/$',views.SetComment, {'blog_type': 'C#advance'}),
	url(r'newcomment/Bootstrapblog/(?P<blogid>\d*)/$',views.SetComment, {'blog_type': 'Bootstrap'}),
	url(r'newcomment/ubuntublog/(?P<blogid>\d*)/$',views.SetComment, {'blog_type': 'ubuntu'}),
	# url(r'findpassword/$', views.SendMail),
	# url(r'checkcode/$', views.CheckCode),
	
]