from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.test, name='test'),
	url(r'^car/(?P<pk>[0-9]+)/$',views.car_details, name='car_details'),
]
