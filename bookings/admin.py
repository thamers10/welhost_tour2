from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('tourist', 'service', 'date', 'status')
    list_filter = ('status', 'date')
    search_fields = ('tourist__username', 'service__user__username')
