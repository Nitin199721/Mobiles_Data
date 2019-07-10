from django.urls import path, re_path
from . import views


urlpatterns = [

    path('', views.get_url, name='index'),
    re_path(r'^list/(?P<name>[\w\-]+)/$', views.list_phone),

    # path('/name<int: name>', views.list_phone, name='lists'),

]
