from case.models import Case, Status, CaseInfo
from caseworker.models import Company
from django.shortcuts import render
from django import forms
from extra_views import ModelFormSetView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
)



class CaseInline(InlineFormSetFactory):
    model = Case
    fields = ['title', 'description', 'case_info']


class CaseCreateView2(CreateWithInlinesView):
    model = CaseInfo
    fields = ['company', 'status']

    inlines = [CaseInline]
    template_name = 'case/formset.html'

    # context_object_name = 'Case'










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
    context_object_name = 'Cases'
    fields = ['title', 'description', 'case_info']


class CaseDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = Case
    success_url = '/case'


def CaseCreatNew(request, **kwargs):
    context = {
        "case_info": CaseInfo.objects.get(id=1)
    }
    return render(request, 'case/case_new_form.html', context)
