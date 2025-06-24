from django.shortcuts import render
from services.models import ServiceItem

# ✅ الصفحة الرئيسية: تعرض صورة رئيسية + بعض الخدمات (مختصرة)
def home(request):
    image_path = "/service_images/91222970-11d8-4b60-ac35-45b5e2e6529e.jfif"

    try:
        services = ServiceItem.objects.all()[:6]  # عرض أول 6 خدمات فقط
    except Exception as e:
        services = []
        print("⚠️ خطأ في جلب الخدمات:", e)

    return render(request, "home.html", {
        "image_path": image_path,
        "services": services,
    })


# ✅ صفحة تعرض جميع الخدمات بالتفصيل
def all_services_view(request):
    try:
        services = ServiceItem.objects.all()
    except Exception as e:
        services = []
        print("⚠️ خطأ في عرض كل الخدمات:", e)

    return render(request, "services/all_services.html", {
        "services": services
    })
