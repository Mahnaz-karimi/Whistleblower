from case.models import Case, Status  # CaseInfo  # , Company
# from django import forms

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


class CaseCreateView(CreateView):

    template_name = 'case/case_form.html'
    model = Case
    fields = ['title', 'description', 'case_info']
    # widgets = {'case_info': forms.HiddenInput(instance=CaseInfo.objects.get(id=3))}


class CaseDeleteView(DeleteView):
    template_name = 'case/case_confirm_delete.html'
    model = Case
    success_url = '/case'


class ReportCreateView(CreateView):
    template_name = 'case/case_form.html'
    model = Case
    fields = ['title', 'description', 'case_info']


'''
from django.contrib.auth.decorators import login_required
@login_required
def case_form_view(request):
    anonymous_form = AnonymousForm(request.POST or None)
    request.session['company_guid'] = 'invalid'

    if (request.method == 'POST'):
        if anonymous_form.is_valid():
            guid = anonymous_form.cleaned_data['guid']
            try:
                company_object = Company.objects.filter(guid=guid).get()
                if not company_object:
                    return redirect('home_view')
                else:
                    request.session['company_guid'] = 'valid'
                    return redirect('case_view')
            except:
                return redirect('home_view')


    home_context = {

    }

    return render(request, "home.html", home_context)

from django.shortcuts import redirect, render


def home(request):
    context = {
        "cases": Case.objects.all()
        # "cases": Case.objects.filter(title="file").order_by('case_post')[:2]  # kallder alle ellementer
    }
    return render(request, "case/case.html", context)
'''
