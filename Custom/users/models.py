from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.TextField(null=True, blank=True) # номер телефона пользователя
    age = models.PositiveIntegerField(null=True, blank=True) # возраст пользователя
    salary_amount = models.FloatField(null=True, blank=True) # зарплата пользователя