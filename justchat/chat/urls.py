from django.urls import path , re_path
from .views import index,room
from . import views
from django.conf.urls import url
app_name = 'chat'

urlpatterns = [
    url(r'^$',views.index,name="index"),
    #path( '^$', views.index , name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
