
from django.urls import re_path as url
from EmployeeApp import views

urlpatterns =[
    url(r'^department$', views.department_api),
    url(r'^department/([0-9]+)$', views.department_api)
 ]