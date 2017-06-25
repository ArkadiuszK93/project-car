from django.conf.urls import url, include
from django.contrib import admin
from app1 import views
from django.contrib.auth import views as auth_views


urlpatterns = [
 	url(r'^cars/', include('app1.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^filter/(?P<form>)/$', views.filter, name='car_edit'),
	url(r'^filter/$', views.car_filter, name='car_filter'),
	url(r'^$',views.index, name ="index"),
	#url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
	url(r'^login/$', auth_views.login , name="login"   ),
	url(r'^user/$', views.user_details, name="user_details"),
	url(r'^register/$' ,views.register, name="register")


    #app1
   # url(r'^$',views.test, name='test'),
	#url(r'^car/(?P<pk>[0-9]+)/$',views.car_details, name='car_details'),
]
