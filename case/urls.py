from django.urls import path
from case.views import CaseDetailView, CaseDeleteView, CaseNewCreateView, \
    CaseInfoListView, CaseInfoCasesListView, CaseInfoDeleteView, ReportCreateView, \
    ReportLoginView, CaseInfoUpdateView, RevisitCaseInfoView, RevisitLoginView, RevisitCaseNewCreateView
from django.contrib.auth.decorators import login_required


app_name = "case"
urlpatterns = [
    path('', login_required(CaseInfoListView.as_view()), name='caseinfo-view'),
    path('<int:id>/caseinfo/cases/', login_required(CaseInfoCasesListView.as_view()), name='caseinfo-cases-view'),
    path('<int:pk>/', login_required(CaseDetailView.as_view()), name='case-detail'),
    path('<int:id>/new/', login_required(CaseNewCreateView.as_view()), name='case-create-new'),
    path('<int:pk>/delete/', login_required(CaseDeleteView.as_view()), name='case-delete'),
    path('<int:pk>/delete/caseinfo/', login_required(CaseInfoDeleteView.as_view()), name='caseinfo-delete'),

    path('<int:id>/new/report/', ReportCreateView.as_view(), name='new-report'),
    path('login/', ReportLoginView.as_view(), name='report-login'),
    path('post/<int:pk>/update/', CaseInfoUpdateView.as_view(), name='caseinfo-update'),
    path('login/revisit/', RevisitLoginView.as_view(), name='revisit-login'),
    path('<int:id>/revisit/report/', RevisitCaseInfoView.as_view(), name='revisit-report'),
    path('<int:id>/revisit/new/', RevisitCaseNewCreateView.as_view(), name='revisit-case-new'),
]
