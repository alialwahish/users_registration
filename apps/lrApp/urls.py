from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^success$',views.success),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^reset$',views.delete)
]

    #/(?P<id>\d+)