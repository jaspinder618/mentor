from django.urls import path
from .views import *

urlpatterns = [
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('courses/',courses, name='courses'),
    path('courses/<str:trainer>',tcourses, name='tcourses'),
    path('details/<int:id>',detail, name='detail'),
    path('events/',events, name='events'),
    path('',index, name='index'),
    path('pricing/',pricings, name='pricing'),
    path('trainers/',trainers, name='trainers'),
]