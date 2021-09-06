from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    else:
        form = UserLoginForm()
        context = {'title': 'Login',
                       'form': form}
        return render(request, 'users/login.html', context)


def registration(request):
    form = UserLoginForm(data=request.POST)
    context = {'title': 'Create Account',
               'form': form}
    return render(request, 'users/register.html', context)
