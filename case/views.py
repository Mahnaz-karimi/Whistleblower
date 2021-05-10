from case.models import Case  # , Status, CaseInfo, Company

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)


class CaseListView(ListView):
    model = Case
    template_name = 'case/case.html'
    context_object_name = 'Case'
    ordering = ['-created']


class CaseDetailView(DetailView):
    model = Case
    template_name = 'case/case_detail.html'


class CaseCreateView(CreateView):
    template_name = 'case/case_form.html'
    model = Case
    fields = ['title', 'description', 'case_info']


'''
from django.shortcuts import redirect, render
def home(request):
    context = {
        "cases": Case.objects.all()
        # "cases": Case.objects.filter(title="file").order_by('case_post')[:2]  # kallder alle ellementer
    }
    return render(request, "case/case.html", context)
'''
