from django.contrib import admin
from django.utils.html import format_html
from .models import ServiceProfile, ServiceItem, Review


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1
    fields = ('name', 'price', 'image', 'preview_image', 'cloudinary_url')
    readonly_fields = ('preview_image', 'cloudinary_url')
    show_change_link = True

    def preview_image(self, obj):
        if obj.cloudinary_url:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" width="80" height="60" style="object-fit: cover; border-radius: 4px;" /></a>',
                obj.cloudinary_url
            )
        return "لا توجد صورة"
    preview_image.short_description = "معاينة الصورة"


@admin.register(ServiceProfile)
class ServiceProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'price_per_day', 'available')
    search_fields = ('user__username', 'city')
    list_filter = ('available',)
    inlines = [ServiceItemInline]


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile', 'price', 'preview_image')
    search_fields = ('name', 'profile__user__username')
    list_filter = ('price',)
    readonly_fields = ('preview_image', 'cloudinary_url')
    fields = ('name', 'price', 'image', 'preview_image', 'cloudinary_url')

    def preview_image(self, obj):
        if obj.cloudinary_url:
            return format_html(
                '<a href="{0}" target="_blank">'
                '<img src="{0}" width="80" height="60" style="object-fit: cover; border-radius: 4px;" /></a>',
                obj.cloudinary_url
            )
        return "لا توجد صورة"
    preview_image.short_description = "معاينة الصورة"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'service', 'rating', 'created_at')
    search_fields = ('reviewer__username', 'service__user__username')
    list_filter = ('rating', 'created_at')
