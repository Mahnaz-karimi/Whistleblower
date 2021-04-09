from django.shortcuts import render, redirect
from django.contrib import messages
from caseworker.models import CaseworkerAdmin


def register(request):
    if request.method == 'POST':
        form = CaseworkerAdmin(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = CaseworkerAdmin()
    return render(request, 'caseworker/register.html', {'form': form})
