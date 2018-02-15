from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^newform$', views.newform, name='newform'),
    url(r'^sentmsg$', views.sent_msg, name='sent_msg'),
    url(r'^post/(?P<id>[0-9]+)/$', views.delete_msg, name='delete_msg'),
    url(r'^$', views.index, name='index'),
]
