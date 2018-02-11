from django.conf.urls import url, include
from . import views

#url
urlpatterns = [
        url(r'^$', views.index, name='index'),
]
