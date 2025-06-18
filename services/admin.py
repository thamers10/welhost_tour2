from django.contrib import admin
from .models import ServiceProfile, Review

@admin.register(ServiceProfile)
class ServiceProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'price_per_day', 'available')
    search_fields = ('user__username', 'city')
    list_filter = ('available',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'service', 'rating', 'created_at')
    search_fields = ('reviewer__username', 'service__user__username')
