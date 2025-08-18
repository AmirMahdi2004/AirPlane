from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users_create/', views.user_create, name='user_create'),
    path('users_edit/<int:pk>/', views.user_edit, name='user_edit'),
    # path("register/", views.register, name="signup"),
    path('request_register/', views.request_register, name='request_register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ticket/', views.ticket, name='ticket'),
    path('waiting/', views.waiting_page, name='waiting'),

]
