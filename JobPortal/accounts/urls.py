from django.urls import path
from . import views

urlpatterns = [
    path('jobseeker/register/', views.jobseeker_register, name ='jobseeker_register'),
    path('employer/register/', views.employer_register, name ='employer_register'),
    path('login/', views.login_view, name='login'),
    path('jobseeker/dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
    path('employer/dashboard/', views.employer_dashboard, name='employer_dashboard'),
]
