from django.db import models
from accounts.models import User

class ServiceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    languages = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s Service"

class Review(models.Model):
    service = models.ForeignKey(ServiceProfile, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} rated {self.service.user.username}"
