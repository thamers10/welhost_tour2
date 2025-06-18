from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView  # ← لإظهار صفحة HTML ثابتة

urlpatterns = [
    path('admin/', admin.site.urls),

    # صفحة رئيسية من قالب HTML
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # توجيه التطبيقات الثلاثة
    path('api/accounts/', include('accounts.urls')),
    path('api/bookings/', include('bookings.urls')),
    path('api/services/', include('services.urls')),
]
