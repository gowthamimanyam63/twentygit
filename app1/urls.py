from django.urls import path
from app1.views import *
app_name='anything2'
urlpatterns=[
    path('specificstatic2/',specificstatic2,name='specificstatic2'),
]