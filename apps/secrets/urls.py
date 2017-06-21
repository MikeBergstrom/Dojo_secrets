from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^secrets$', views.secrets),
    url(r'^process$', views.process),
    url(r'like/(?P<source>\w+)/(?P<id>\d+)$', views.like),
    url(r'delete/(?P<source>\w+)/(?P<id>\d+)$', views.delete),
    url(r'^popular$', views.popular),
    url(r'^logout$', views.logout)
]