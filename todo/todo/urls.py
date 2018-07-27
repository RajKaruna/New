
from django.conf.urls import url
from django.contrib import admin
from todo_list import views
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('',include('todo_list.urls')),

]
