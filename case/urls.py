from django.urls import path
from case.views import CaseListView, CaseDetailView, CaseCreateView, CaseDeleteView
from django.contrib.auth.decorators import login_required


app_name = "case"
urlpatterns = [
    path('', login_required(CaseListView.as_view()), name='case-view'),
    path('<int:pk>/', login_required(CaseDetailView.as_view()), name='case-detail'),
    path('new/', login_required(CaseCreateView.as_view()), name='case-create'),
    path('<int:pk>/delete/', login_required(CaseDeleteView.as_view()), name='case-delete'),
]
