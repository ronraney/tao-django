from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    #path('/post', views.post, name='post'),
    #path('/tao', views.tao name='tao'),
    #path('/recovery', views.recovery, name='recovery'),
    #path('taorecovery', views.taorecovery, name='taorecovery'),
    #path('contact', views.contact, name='contact'),
]