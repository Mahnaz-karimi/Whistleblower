from django.urls import path
from case.views import CaseListView, CaseDetailView, CaseCreateView, CaseDeleteView


app_name = "case"
urlpatterns = [
    path('', CaseListView.as_view(), name='case-view'),
    path('case/<int:pk>/', CaseDetailView.as_view(), name='case-detail'),
    path('case/new/', CaseCreateView.as_view(), name='case-create'),
    path('case/<int:pk>/delete/', CaseDeleteView.as_view(), name='case-delete'),
]
