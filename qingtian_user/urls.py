from django.conf.urls import url
from qingtian_user import views

urlpatterns = [
	url(r'newuser/$', views.Register),
	url(r'loginservice/$', views.Login),
	url(r'logoutservice/$', views.Logout),
	url(r'findpassword/$', views.SendMail),
	url(r'checkcode/$', views.CheckCode),
	
]