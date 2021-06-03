from case.models import Case, Status  # , CaseInfo, Company
# from django.shortcuts import render
# from extra_views import CreateWithInlinesView, InlineFormSetFactory

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
    context_object_name = 'Cases'
    fields = ['title', 'description', 'case_info']


class CaseDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = Case
    success_url = '/case'
