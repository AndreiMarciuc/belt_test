from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$',views.index),
    url(r'^create$',views.create),
    url(r'^add/(?P<id>\d+)$',views.addQuote),
    url(r'^remove/(?P<id>\d+)$',views.removeQuote),
    url(r'^show/(?P<id>\d+)$',views.showUser),
    

]
