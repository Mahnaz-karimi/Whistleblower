# from django.shortcuts import render
from case.models import Case, CaseInfo, Status, Media
# import uuid
from django.views.generic import (
    ListView,
    DetailView,  # når vil kigges efter detail of post
    CreateView,
    # UpdateView,
    # DeleteView
)
# from django.http import HttpResponse

'''
def home(request):
    context = {
        "cases": Case.objects.all()
        # "cases": Case.objects.filter(title="file").order_by('case_post')[:2]  # kallder alle ellementer
    }
    return render(request, "case/case.html", context)
'''


class CaseListView(ListView):
    model = Case
    template_name = 'case/case.html'
    context_object_name = 'Case'
    ordering = ['-created']


class CaseDetailView(DetailView):
    model = Case


class CaseCreateView(CreateView):
    status = Status.objects.create()
    case_info = CaseInfo.objects.create(status=status)
    model = Case(case_info)
    fields = ['title', 'description']

    '''def form_valid(self, form):
        form.instance.author = self.request.user  # tjekker at den er aktuelle user
        return super().form_valid(form)'''
