from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm
from .models import User


@require_http_methods(["GET", "POST"])
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"👋 مرحبًا {user.first_name or user.username}، تم تسجيل الدخول بنجاح!")

            # إعادة التوجيه حسب الدور
            if user.role == "guide":
                return redirect("guide_list")
            elif user.role == "driver":
                return redirect("driver_list")
            else:
                return redirect("home")  # عدّل حسب الصفحة الرئيسية للسياح
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة.")

    return render(request, "accounts/login.html", {"form": form})


@require_http_methods(["GET", "POST"])
def signup_view(request):
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "🎉 تم إنشاء الحساب بنجاح!")

            # إعادة التوجيه حسب الدور
            if user.role == "guide":
                return redirect("guide_list")
            elif user.role == "driver":
                return redirect("driver_list")
            else:
                return redirect("home")
        else:
            messages.error(request, "❌ هناك خطأ في البيانات، الرجاء التحقق.")

    return render(request, "accounts/signup.html", {"form": form})


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح.")
    return redirect("login")
