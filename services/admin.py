from django.contrib import admin
from .models import ServiceProfile, ServiceItem, Review


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1  # عدد الحقول الفارغة الجاهزة للإضافة
    fields = ('name', 'image', 'price')
    readonly_fields = ()
    show_change_link = True


@admin.register(ServiceProfile)
class ServiceProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'price_per_day', 'available')
    search_fields = ('user__username', 'city')
    list_filter = ('available',)
    inlines = [ServiceItemInline]


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'price')
    search_fields = ('name', 'profile__user__username')
    list_filter = ('price',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'service', 'rating', 'created_at')
    search_fields = ('reviewer__username', 'service__user__username')
    list_filter = ('rating', 'created_at')
