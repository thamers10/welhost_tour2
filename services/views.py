from django.shortcuts import render
from services.models import ServiceItem

# ✅ الصفحة الرئيسية: تعرض صورة رئيسية + جميع الخدمات بشكل مختصر
def home(request):
    image_path = "/service_images/91222970-11d8-4b60-ac35-45b5e2e6529e.jfif"

    services = ServiceItem.objects.select_related('profile__user').all()

    return render(request, "home.html", {
        "image_path": image_path,
        "services": services  # يجب أن يتطابق مع ما يُستخدم داخل قالب include
    })


# ✅ صفحة منفصلة لعرض جميع الخدمات (مثلاً عند زيارة: /api/services/all/)
def all_services_view(request):
    services = ServiceItem.objects.select_related('profile__user').all()

    return render(request, "services/all_services.html", {
        "services": services
    })
