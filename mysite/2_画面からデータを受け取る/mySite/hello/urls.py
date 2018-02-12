from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get/$', views.hello_get_query, name='hello_get_query'),
]