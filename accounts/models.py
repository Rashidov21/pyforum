from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    address = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='user_images/', blank=True)
    bio = models.TextField(blank=True)
    facebook_link = models.URLField(verbose_name="Facebook link", blank=True)
    instagram_link = models.URLField(verbose_name="Instagram link", blank=True)
    telegram_link = models.URLField(verbose_name="Telegram link", blank=True)

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        else:
            return "No fullname"

    def __str__(self):
        return str(self.username)
