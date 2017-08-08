from django.conf.urls import url

from . import views

app_name='hello'
urlpatterns = [
    url(r'^$', views.hello, name='hello'),
]
