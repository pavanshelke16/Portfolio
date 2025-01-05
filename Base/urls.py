from django.urls import path 
from . import views

urlpatterns=[
    path('',views.contact, name='home'),
    # path('contact/',views.contact,name="savecontact")
]
