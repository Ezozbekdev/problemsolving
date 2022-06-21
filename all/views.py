import os.path
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .models import Problem
from django.views.generic.detail import DetailView
from django.http import Http404, HttpResponse
from django.conf import settings
from .forms import CreateUserForm
from django.contrib import messages


def loginviews(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, 'username or password is incorrect')
            return render(request, 'all/login.html', context)

    return render(request, 'all/login.html', context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')
    context = {'form': form}
    return render(request, 'all/register.html', context)


class Detail_Views(DetailView):
    model = Problem
    template_name = 'all/detail.html'
    context_object_name = 'obj'


def prblem(request):
    search = request.GET.get('search')
    if search:
        model = Problem.objects.filter(title__contains=search)
    else:
        model = Problem.objects.all()

    context = {
        'problems': model,
        'search': search
    }
    return render(request, 'all/index.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response
    raise Http404
