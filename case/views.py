from case.models import Case, Status, CaseInfo, Company
from django.http import HttpResponse
from django import forms
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)


class CaseListView(ListView):
    model = Case
    template_name = 'case/case.html'
    context_object_name = 'Case'
    ordering = ['-created']


class CaseDetailView(DetailView):
    model = Case
    template_name = 'case/case_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deletable_state = Status.CASESTATUS[0][1]
        context['deletable'] = (str(self.object.case_info.status) == deletable_state)
        return context


class CaseCreateView(CreateView, ListView):
    template_name = 'case/case_form.html'
    model = Case
    fields = ['title', 'description']
    context_object_name = 'Cases'


class CaseDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = Case
    success_url = '/case'


def CaseCreatNew(request, **kwargs):
    context = {
        "case_info": CaseInfo.objects.get(id=3)
    }
    return render(request, 'case/case_new_form.html', context)

