from django.urls import path
from . import views



urlpatterns = [
    path('login', views.login ,name='login'),
    path('register', views.register ,name='register'),
    path('logout_user', views.logout_user ,name='logout_user'),

    path('dashboard', views.dashboard ,name='dashboard'),
   
    # path('about/', views.about ,name='about'),
    # path('services/', views.services ,name='services'),
    # path('contact/', views.contact ,name='contact'),
] 
