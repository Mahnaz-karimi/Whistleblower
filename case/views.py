from django.shortcuts import get_object_or_404
from case.models import Case, Status, CaseInfo, Company
from django.shortcuts import redirect, render
from case.forms import AnonymousForm
from django.urls import reverse
# from django.http import HttpResponse
# from django.shortcuts import render
# from extra_views import CreateWithInlinesView, InlineFormSetFactory
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    FormView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


class CaseInfoListView(ListView):
    model = CaseInfo
    template_name = 'case/caseinfo.html'
    context_object_name = 'CaseInfo'


class CaseInfoCasesListView(ListView):
    model = Case
    template_name = 'case/caseinfo_cases.html'

    def get_context_data(self, **kwargs):
        context = super(CaseInfoCasesListView, self).get_context_data(**kwargs)
        case_info = get_object_or_404(CaseInfo, id=self.kwargs['id'])
        print("Case info ", case_info)
        context['Case'] = Case.objects.filter(case_info=case_info.id)
        print(Case.objects.filter(case_info=case_info.id))
        return context


class CaseInfoDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = CaseInfo
    success_url = '/case'


class CaseNewCreateView(CreateView):
    template_name = 'case/case_new_caseworker.html'
    model = Case
    fields = ['title', 'description']

    def form_valid(self, form):
        case_info = get_object_or_404(CaseInfo, id=self.kwargs['id'])
        form.instance.case_info = case_info
        return super(CaseNewCreateView, self).form_valid(form)


class CaseDetailView(DetailView):
    model = Case
    template_name = 'case/case_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        deletable_state = Status.CASESTATUS[0][1]
        context['deletable'] = (str(self.object.case_info.status) == deletable_state)
        return context


class CaseDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = Case
    success_url = '/case'


class ReportLoginView(FormView):
    template_name = 'case/report_login.html'
    form_class = AnonymousForm

    def post(self, request, *args, **kwargs):
        form = AnonymousForm(request.POST)
        guid = form['guid'].data
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template_name, context)
        try:
            company = Company.objects.get(guid=guid)  # Kaster en undtagelse hvis company.guid er ukendt
            status = Status.objects.create()
            case_info = CaseInfo.objects.create(status=status, company=company)
            case_info.save()
            context = {'case_info': case_info}
            request.session['cmp_guid'] = 'valid'
            case_create_url = reverse('case:new-report', args=[case_info.id])
            return redirect(case_create_url, context)
        except Company.DoesNotExist:
            return redirect('case:report-login')


class ReportCreateView(CreateView):
    model = Case
    fields = ['title', 'description']

    def get(self, request, *args, **kwargs):
        if 'cmp_guid' in self.request.session:
            if self.request.session['cmp_guid'] == 'valid':
                del request.session['cmp_guid']
                return render(request, 'case/report_form.html')
        else:
            return redirect(reverse('case:report-login'))

    def form_valid(self, form):
        case_info = get_object_or_404(CaseInfo, id=self.kwargs['id'])
        form.instance.case_info = case_info
        return super(ReportCreateView, self).form_valid(form)


class CaseInfoUpdateView(UpdateView):  # add mixin hjælper os at postens skaberen får lov til update post
    model = CaseInfo
    fields = ['caseworker', 'status']
    success_url = '/case'
