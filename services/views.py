from django.shortcuts import render

# الصفحة الرئيسية – عرض صورة الخدمة

def home(request):
    image_name = "91222970-11d8-4b60-ac35-45b5e2e6529e.jfif"  # ← عدل هذا الاسم إذا تغيّر
    image_path = f"/service_images/{image_name}"
    return render(request, "home.html", {"image_path": image_path})
