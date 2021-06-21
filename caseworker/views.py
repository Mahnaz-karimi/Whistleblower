from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
)
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from caseworker.forms import CaseworkerAdmin


@login_required
def register(request):
    if request.method == 'POST':
        form = CaseworkerAdmin(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(reverse('case:caseinfo-view'))
    else:
        form = CaseworkerAdmin()
    return render(request, 'caseworker/register.html', {'form': form})


class CaseWorkerListView(ListView):
    model = User
    template_name = 'caseworker/caseworker.html'
    context_object_name = 'User'


class CaseWorkerDetailView(DetailView):
    model = User
    template_name = 'caseworker/caseworker_detail.html'


class LoginView(auth_views.LoginView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['revisible'] = settings.FEATURES.get('REVISIT_CASE')
        return context
