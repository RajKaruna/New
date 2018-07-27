from django.conf.urls import url
from . import views


urlpatterns=[
      
          url(r'delete/(?P<list_id>\d+)$', views.delete, name='delete'),
          url(r'cross_off/(?P<list_id>\d+)$', views.cross_off, name='cross_off'),
          url(r'uncross/(?P<list_id>\d+)$', views.uncross, name='uncross'),
          url(r'edit/(?P<list_id>\d+)$', views.edit, name='edit'),
          url('', views.home, name="home"),
]