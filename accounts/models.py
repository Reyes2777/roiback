from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.utils import IDENTIFICATION_TYPES, GENDER


class CustomUser(AbstractUser):
    birthday_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=50, null=True, blank=True)
    identification_number = models.CharField(max_length=12, null=True, blank=True)
    identification_type = models.CharField(choices=IDENTIFICATION_TYPES, max_length=50, null=True, blank=True)
    mobile_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
