from django.db import models
from accounts.models import User
from services.models import ServiceProfile

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    tourist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(ServiceProfile, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Booking by {self.tourist.username} with {self.service.user.username} on {self.date}"
