from django.shortcuts import render


# Create your views here.

def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin.html', context)


def admins_users(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-read.html', context)


def admins_users_create(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-create.html', context)


def admins_users_update(request, id):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-update-delete.html', context)


def admins_users_delete(request, id):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-update-delete.html', context)
