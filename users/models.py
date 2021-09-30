from datetime import timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.timezone import now


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', default=18)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # activation_key_expires = models.DateTimeField(default=(now()+timedelta(hours=48)))


    def is_activation_key_expires(self):
        if now() <=self.activation_key_expires + timedelta(hours=48):
            return False
        return True