from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forms/$', views.hello_forms, name='hello_forms'), # 追加する
    url(r'^form_samples/$', views.hello_forms2, name='hello_forms2'),  # 追加する
]