from django.urls import path
from case.views import CaseListView, CaseDetailView, CaseCreateView, CaseDeleteView, CaseNewCreateView, \
    CaseInfoListView, CaseInfoCasesListView, CaseInfoDeleteView
from django.contrib.auth.decorators import login_required


app_name = "case"
urlpatterns = [
    path('', login_required(CaseListView.as_view()), name='case-view'),
    path('caseinfo/', login_required(CaseInfoListView.as_view()), name='caseinfo-view'),
    path('<int:id>/caseinfo/cases/', login_required(CaseInfoCasesListView.as_view()), name='caseinfo-cases-view'),
    path('<int:pk>/', login_required(CaseDetailView.as_view()), name='case-detail'),
    path('new/', login_required(CaseCreateView.as_view()), name='case-create'),

    path('<int:id>/new/', login_required(CaseNewCreateView.as_view()), name='case-create-new'),
    path('<int:pk>/delete/', login_required(CaseDeleteView.as_view()), name='case-delete'),
    path('<int:pk>/delete/caseinfo/', login_required(CaseInfoDeleteView.as_view()), name='caseinfo-delete'),

]
