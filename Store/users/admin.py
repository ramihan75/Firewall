from django.contrib import admin
from .models import Store
from .forms import StoreChangeForm, StoreCreationForm


# Низкоуровневый админский интерфейс
from django.contrib.auth.admin import UserAdmin 
# Register your models here.


# Создаем свой интерфейс по взаимодействию с моделью на основе UserAdmin
class StoreAdmin(UserAdmin):
    add_form = StoreCreationForm
    form = StoreChangeForm
    model = Store
    list_display = ["email", "username", "inn", "year_open"]


# Регистрируем интерфейс в панель
admin.site.register(Store, StoreAdmin)
