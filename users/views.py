from django.shortcuts import render

# Create your views here.


def login(request):
    context = {'title':'Login'}
    return render(request, 'users/login.html', context)

def registration(request):
    context = {'title': 'Create Account'}
    return render(request, 'users/register.html', context)