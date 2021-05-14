from case.models import Case  # , Status, CaseInfo, Company
from django.shortcuts import redirect, render
from case.forms import AnonymousForm
from caseworker.models import Company
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
