from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import CustomUser


# def register(request):
#     if request.method == 'POST':
#         form = CreateUserFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user_list')
#     else:
#         form = CreateUserFrom()
#     context = {'form': form}
#     return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.role == 'admin':
                return redirect('user_list')
            else:
                return redirect('mp')
        else:
            return render(request, 'accounts/login.html', {'error': 'نام کاربری یا رمز عبور اشتباه است'})
    return render(request, 'accounts/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def user_list(request):
    if request.user.role == 'admin':
        userlist = CustomUser.objects.filter(manager=request.user)
        context = {"userlist": userlist}
        return render(request, 'accounts/user_list.html', context)
    else:
        return render(request, 'accounts/access_error.html')


@login_required
def user_create(request):
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_list')
    else:
        form = CreateUserFrom()
    return render(request, 'accounts/user_create.html', {'form': form, 'is_edit': False})


@login_required
def user_edit(request, pk):
    user_obj = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_obj)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserChangeForm(instance=user_obj)
    return render(request, 'accounts/user_edit.html', {'form': form, 'is_edit': True})


@login_required
def user_delete(request, username):
    pass


@login_required
def ticket(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            # ایجاد شی بدون ذخیره
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    else:
        form = SupportTicketForm()
    return render(request, 'accounts/ticket.html', {'form': form})


def request_register(request):
    if request.method == 'POST':
        form = RequestRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waiting')
    else:
        form = RequestRegisterForm()
    return render(request, 'accounts/request_register.html', {'form': form})


def waiting_page(request):
    return render(request, 'accounts/waiting_page.html')
