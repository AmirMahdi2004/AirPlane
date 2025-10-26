from django.urls import path
from . import views

app_name = 'bord'

urlpatterns = [
    path('air', views.airplane_list, name='airplane'),
    path('sll/<pk>/', views.sll_view, name='sll'),
    path('mp/<pk>', views.mp_view, name='mp'),
    path('flt/<pk>', views.flt_view, name='flt'),
    path('flt_form/', views.flt_form, name='flt_form'),
    path('mp_form/', views.mp_form, name='mp_form'),
    path('sll_form/', views.sll_form, name='sll_form'),
    path('input/', views.input_bord, name='input'),

]
