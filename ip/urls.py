from django.conf.urls import patterns, include, url
from ip import views

'''
urlpatterns = patterns('pi.ip.views',
    url(r'^$', 'index'),
    url(r'^list/$', 'list'),
    url(r'^(?P<ip>\s+)/submit/$', 'submit'),
)
'''

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.list, name='list'),
    url(r'^add/(?P<name>\w+)/(?P<ip>\d+\.\d+\.\d+\.\d+)$', views.add, name = 'add'),
)