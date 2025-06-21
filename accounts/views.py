from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm

@require_http_methods(["GET", "POST"])
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('home')  # عدّل اسم الصفحة الرئيسية حسب الحاجة

    return render(request, 'accounts/login.html', {'form': form})


@require_http_methods(["GET", "POST"])
def signup_view(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')  # عدّل اسم الصفحة الرئيسية حسب الحاجة

    return render(request, 'accounts/signup.html', {'form': form})


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return redirect('login')
