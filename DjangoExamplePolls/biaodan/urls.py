from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^$', views.get_name, name='get_name')
]
