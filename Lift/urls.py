from django.conf.urls import url
from Thrust import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
]