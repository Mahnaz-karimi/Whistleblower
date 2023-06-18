from django.http.response import Http404
from django.shortcuts import get_object_or_404
from case.models import Case, Status, CaseInfo, Company
from django.shortcuts import redirect, render
from case.forms import AnonymousForm
from django.urls import reverse
from django.conf import settings
import threading
import time
from pathlib import Path
import os
from django.http import HttpResponse
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
        context['Case'] = Case.objects.filter(case_info=case_info.id)
        return context


class CaseInfoDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = CaseInfo
    success_url = '/case/'


class CaseInfoUpdateView(UpdateView):
    model = CaseInfo
    fields = ['caseworker', 'status']
    success_url = '/case/'
    template_name = 'case/caseinfo_form.html'


class CaseNewCreateView(CreateView):
    template_name = 'case/case_new_caseworker.html'
    model = Case
    fields = ['title', 'description']
    success_url = '/case/'

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
        context['editable'] = settings.FEATURES.get('EDIT_CASE')
        return context


class CaseDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = Case
    success_url = '/case/'


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
                context = {"case_info": get_object_or_404(CaseInfo, id=self.kwargs['id'])}
                return render(request, 'case/report_form.html', context)
        else:
            return redirect(reverse('case:report-login'))

    def form_valid(self, form):
        case_info = get_object_or_404(CaseInfo, id=self.kwargs['id'])
        form.instance.case_info = case_info
        return super(ReportCreateView, self).form_valid(form)


class RevisitLoginView(FormView):
    template_name = 'case/revisit_login.html'
    form_class = AnonymousForm

    def post(self, request, *args, **kwargs):
        form = AnonymousForm(request.POST)
        guid = form['guid'].data
        if not form.is_valid():
            context = {'form': form}
            return render(request, self.template_name, context)
        try:
            case_info = CaseInfo.objects.get(guid=guid)
        except CaseInfo.DoesNotExist:
            return redirect('case:report-login')

        context = {'case_info': case_info}
        request.session['case_guid'] = 'valid'
        case_create_url = reverse('case:revisit-report', args=[case_info.id])
        return redirect(case_create_url, context)


class RevisitCaseInfoView(ListView):
    model = CaseInfo
    template_name = 'case/revisit_report.html'

    def get_context_data(self, **kwargs):
        if 'case_guid' in self.request.session:
            if self.request.session['case_guid'] == 'valid':
                try:
                    context = super().get_context_data(**kwargs)
                    self.CaseInfo = get_object_or_404(CaseInfo, id=self.kwargs['id'])
                    context['case_info'] = self.CaseInfo
                    context['cases'] = Case.objects.filter(case_info=self.CaseInfo.id).order_by('-created')
                    context['deletable'] = (str(self.CaseInfo.status) == Status.CASESTATUS[0][1])
                    del self.request.session['case_guid']
                    self.request.session['info_guid'] = 'valid'
                    return context

                except:
                    raise Http404()

        else:
            raise Http404()


class RevisitCaseNewCreateView(CreateView):
    model = Case
    fields = ['title', 'description']

    def get(self, request, *args, **kwargs):
        if 'info_guid' in self.request.session:
            if self.request.session['info_guid'] == 'valid':
                del request.session['info_guid']
                return render(request, 'case/revisit_case_new.html')
            else:
                return redirect(reverse('case:report-login'))


    def form_valid(self, form ):
        self.CaseInfo = get_object_or_404(CaseInfo, id=self.kwargs['id'])
        form.instance.case_info = self.CaseInfo

        title = form.cleaned_data['title']
        description = form.cleaned_data['description']

        filename = f"{self.CaseInfo.guid}.txt" if self.CaseInfo.guid else "anonymous.txt"

        # Get the user's home directory
        home_dir = str(Path.home())
        # Construct the path to the documents folder
        documents_path = os.path.join(home_dir, 'Documents')

        # Write the initial title and description to a file
        file_path = os.path.join(documents_path, filename)

        # Start a background thread to update the file periodically
        thread = threading.Thread(target=overwrite_file_periodically, args=(file_path, title, description))
        thread.start()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.CaseInfo = get_object_or_404(CaseInfo, id=self.kwargs['id'])
        filename = f"{self.CaseInfo.guid}.txt" if self.CaseInfo.guid else "anonymous.txt"
        home_dir = str(Path.home())
        documents_path = os.path.join(home_dir, 'Documents')
        file_path = os.path.join(documents_path, filename)
        file_content = retrieve_file_content(file_path)
        print ("file_content", file_content)
        context['file_content'] = file_content

        return context

def retrieve_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def update_file_content(file_path, title, description):
    with open(file_path, 'w') as file:
        file.write(f"Title: {title}\nDescription: {description}")

# Define a function to be called periodically
def overwrite_file_periodically(file_path, title, description):
    # Initial file update
    update_file_content(file_path, title, description)

    # Wait for 1-second and update the file again
    time.sleep(1)
    overwrite_file_periodically(file_path, title, description)