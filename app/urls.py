from django.urls import path
from app.views import *
app_name='anything1'
urlpatterns=[
    path('specificstatic1/',specificstatic1,name='specificstatic1'),
]