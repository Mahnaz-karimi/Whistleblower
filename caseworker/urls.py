from django.urls import path
from .views import register


app_name = "case_worker"
urlpatterns = [
    path('register/', register, name='register'),
]
