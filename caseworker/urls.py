from django.urls import path
from caseworker.views import register, CaseWorkerListView, CaseWorkerDetailView, LoginView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = "caseworker"
urlpatterns = [
    path('register/', register, name='register'),
    path('', LoginView.as_view(template_name='caseworker/login.html'), name='login'),
    path('logout/', login_required(auth_views.LogoutView.as_view(template_name='caseworker/logout.html')),
         name='logout'),
    path('caseworker/', login_required(CaseWorkerListView.as_view()), name='caseworker'),
    path('<int:pk>/caseworker/detail/', login_required(CaseWorkerDetailView.as_view()), name='caseworker-detail'),
]
