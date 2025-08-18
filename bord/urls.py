from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_life_limited_view, name='SLL'),
    path('mp/', views.mp_view, name='mp'),
    path('flt/', views.flt, name='flt'),
    path('flt_form/', views.flt_view, name='flt_form'),

]
