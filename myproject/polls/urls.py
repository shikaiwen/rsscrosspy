from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^chrome_kquery/saveword', views.saveword, name='saveword'),
    url(r'^chrome_kquery/wordexists/(?P<user_id>.*)', views.wordexists, name='wordexists'),
]