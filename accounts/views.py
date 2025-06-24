from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm
from .models import User
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

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
                return redirect("home")
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

@require_http_methods(["GET", "POST"])
def contact_view(request):
    if request.method == "POST":
        # هنا ممكن نضيف منطق إرسال بريد أو حفظ بيانات التواصل
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # يمكن تخزينها لاحقًا أو إرسالها

    return render(request, "accounts/contact.html")

# ✅ عرض قائمة المرشدين مع فلتر المدينة
def guide_list(request):
    city = request.GET.get('city')
    guides = User.objects.filter(role='guide')
    if city:
        guides = guides.filter(city=city)

    cities = User.objects.filter(role='guide').values_list('city', flat=True).distinct()
    return render(request, 'accounts/guide_list.html', {
        'guides': guides,
        'cities': cities,
        'selected_city': city,
    })


# ✅ عرض قائمة السائقين مع فلتر المدينة
def driver_list(request):
    city = request.GET.get('city')
    drivers = User.objects.filter(role='driver')
    if city:
        drivers = drivers.filter(city=city)

    cities = User.objects.filter(role='driver').values_list('city', flat=True).distinct()
    return render(request, 'accounts/driver_list.html', {
        'drivers': drivers,
        'cities': cities,
        'selected_city': city,
    })
