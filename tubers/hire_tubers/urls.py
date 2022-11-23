from django.urls import path
from . import views



urlpatterns = [
    path('', views.hire_tubers ,name='hire_tubers'),
 
] 
