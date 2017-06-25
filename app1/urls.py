from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.test, name='test'),
	url(r'^(?P<pk>[0-9]+)/$',views.car_details, name='car_details'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.car_edit, name='car_edit'),
	url(r'^(?P<pk>\d+)/remove/$', views.car_remove, name='car_remove'),
	url(r'^add/$', views.car_add, name='car_add'),
	url(r'^marka/add/$', views.marka_add, name='marka_add'),
]
