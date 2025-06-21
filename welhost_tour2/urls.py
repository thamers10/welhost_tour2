from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from services import views as service_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', service_views.home, name='home'),

    # صفحات المستخدم (تسجيل، تسجيل دخول)
    path('accounts/', include('accounts.urls')),

    # مسارات API
    path('api/bookings/', include('bookings.urls')),
    path('api/services/', include('services.urls')),
]

# دعم ملفات الوسائط أثناء التطوير (الصور وغيرها)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
