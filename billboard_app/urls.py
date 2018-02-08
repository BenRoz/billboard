from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newform$', views.newform, name='newform'),
    url(r'^sentmsg$', views.sent_msg, name='sent_msg'),
    url(r'^post/(?P<id>[0-9]+)/$', views.delete_msg, name='delete_msg')
]