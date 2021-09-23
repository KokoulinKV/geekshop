from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from admins.forms import UserAdminsRegistrationForm, UserAdminsProfileForm, ProductAdminsCreationForm
from products.models import Product
from users.models import User


# Create your views here.

def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin.html', context)

class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)

#
# @user_passes_test(lambda u: u.is_superuser)
# def admins_users(request):
#     context = {
#         'title': 'GeekShop - Admin',
#         'users': User.objects.all()
#     }
#     return render(request, 'admins/admin-users-read.html', context)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminsRegistrationForm
    success_url =reverse_lazy('admins:admins_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_superuser)
# def admins_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminsRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admins_users'))
#     else:
#         form = UserAdminsRegistrationForm()
#     context = {'title': 'GeekShop - Admin',
#                'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


class UserAdminView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminsProfileForm
    success_url = reverse_lazy('admins:admins_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserAdminView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminView, self).dispatch(request, *args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def admins_users_update(request, id):
#     user_select = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminsProfileForm(data=request.POST, instance=user_select, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admins_users'))
#     else:
#         form = UserAdminsProfileForm(instance=user_select)
#     context = {
#         'title': 'GeekShop - Admin',
#         'form': form,
#         'user_select': user_select
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)

class UserAdminDelete(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminsProfileForm
    success_url = reverse_lazy('admins:admins_users')


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminDelete, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

# @user_passes_test(lambda u: u.is_superuser)
# def admins_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admins_users'))

class UserAdminRehub(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminsProfileForm
    success_url = reverse_lazy('admins:admins_users')


    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserAdminRehub, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@user_passes_test(lambda u: u.is_superuser)
def admins_users_rehub(request, id):
    user = User.objects.get(id=id)
    user.is_active = True
    user.save()
    return HttpResponseRedirect(reverse('admins:admins_users'))


def admins_products(request):
    context = {
        'title': 'GeekShop - Admin',
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-products-read.html', context)

def admins_products_create(request):
    if request.method == 'POST':
        form = ProductAdminsCreationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_products'))
    else:
        form = ProductAdminsCreationForm()
    context = {'title': 'GeekShop - Admin',
               'form': form}
    return render(request, 'admins/admin-products-create.html', context)


def admins_products_update(request, id):
    product_select = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductAdminsCreationForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admins_products'))
    else:
        form = ProductAdminsCreationForm(instance=product_select)
    context = {
        'title': 'GeekShop - Admin',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'admins/admin-products-update-delete.html', context)


def admins_products_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(reverse('admins:admins_products'))
