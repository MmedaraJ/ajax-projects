from django.shortcuts import redirect, render, reverse

from .models import Users
from .forms import UsersForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            return
    else:
        form = UsersForm()
    return render(request, 'search/index.html', {'form': form})

def create(request):
    if request.method == 'POST':
        errors = Users.objects.all_validations(request.POST)
        if len(errors):
            for k, v in errors.items(): messages.error(request, v, extra_tags=k)
            return redirect(reverse('search:index'))
        else:
            Users.objects.create(first_name=request.POST['first_name'])
