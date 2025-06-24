from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views


# استيراد العرض الرئيسي من تطبيق الخدمات
from services import views as service_views

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية (تُعرض من تطبيق services)
    path('', service_views.home, name='home'),

    # الحسابات (تسجيل، تسجيل دخول، إلخ)
    path('accounts/', include('accounts.urls')),

    # API للحجوزات
    path('api/bookings/', include('bookings.urls')),

    path('contact/', views.contact_view, name='contact'),


    # API للخدمات
    path('api/services/', include('services.urls')),
]

# دعم ملفات الوسائط في وضع التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
