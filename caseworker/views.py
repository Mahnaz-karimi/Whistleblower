from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from caseworker.forms import CaseworkerAdmin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
)


@login_required
def register(request):
    if request.method == 'POST':
        form = CaseworkerAdmin(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/case')
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
