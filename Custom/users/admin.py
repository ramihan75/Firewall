from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin 

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "age", "username", "is_staff", "phone_number", "salary_amount"]

# Регистрируем интерфейс в панель
admin.site.register(CustomUser, CustomUserAdmin)

