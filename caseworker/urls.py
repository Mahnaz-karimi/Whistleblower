from django.urls import path
from caseworker.views import register
from django.contrib.auth import views as auth_views


app_name = "case_worker"
urlpatterns = [
    path('register/', register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='caseworker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='caseworker/logout.html'), name='logout'),
]
