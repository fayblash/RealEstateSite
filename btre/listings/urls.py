from django.urls import path
from . import views
from .views import *



urlpatterns=[
    path('',views.listings,name='listings'),
    path('<int:listing_id>/listing',views.listing,name='listing'),
    path('search/',views.search,name='search'),
]