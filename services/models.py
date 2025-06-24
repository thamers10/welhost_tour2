from django.db import models
from accounts.models import User
import cloudinary.uploader


class ServiceProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    languages = models.CharField(max_length=255)  # مثال: "العربية, الإنجليزية"
    city = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"الملف المهني لـ {self.user.get_full_name() or self.user.username}"


class ServiceItem(models.Model):
    profile = models.ForeignKey(ServiceProfile, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='temp/', blank=True, null=True)
    cloudinary_url = models.URLField(blank=True, null=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.image:
            result = cloudinary.uploader.upload(self.image)
            self.cloudinary_url = result.get("secure_url")
            self.image = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.profile.user.username}"


class Review(models.Model):
    service = models.ForeignKey(ServiceItem, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer.username} ⭐ {self.rating} → {self.service.name}"
