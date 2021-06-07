from django.urls import path
from . import views
from .views import *

urlpatterns=[
    path('<int:listing_id>/contact',views.contact,name='contact'),
]