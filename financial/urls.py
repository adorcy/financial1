"""
url(r'^customer/new/$', views.customer_new, name='customer_new'),
url(r'^customer/(?P<pk>\d+)/edit/$', views.customer_edit, name='customer_edit'),
url(r'^stock/(?P<pk>\d+)/$', views.stock_detail, name='stock_detail'),
url(r'^stock/new/$', views.stock_new, name='stock_new'),
url(r'^stock/(?P<pk>\d+)/edit/$', views.stock_edit, name='stock_edit'),
url(r'^cryptocurrency/(?P<pk>\d+)/$', views.cryptocurrency_detail, name='cryptocurrency_detail'),
url(r'^cryptocurrency/new/$', views.cryptocurrency_new, name='cryptocurrency_new'),
url(r'^cryptocurrency/(?P<pk>\d+)/edit/$', views.cryptocurrency_edit, name='cryptocurrency_edit'),
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.customer_list, name='customer_list'),
    url(r'^customer/(?P<pk>\d+)/$', views.customer_detail, name='customer_detail'),
]