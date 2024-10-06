from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    name = models.CharField(max_length=100)
    expiry_date = models.DateField()
    added_date = models.DateField(default=timezone.now)

    def days_until_expiry(self):
        """
        Calculate the number of days until expiry for the product.
        """
        today = timezone.now().date()
        return (self.expiry_date - today).days

    def is_expired(self):
        """
        Check if the product is already expired.
        """
        return self.expiry_date < timezone.now().date()

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


