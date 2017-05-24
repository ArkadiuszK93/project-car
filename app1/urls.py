from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.test, name='test'),
	url(r'^car/(?P<pk>[0-9]+)/$',views.car_detail, name='car_detail'),
]
