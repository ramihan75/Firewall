from .models import Store

# Заготовки интерфейса пользовательской модели
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class StoreCreationForm(UserCreationForm):
    """
    Наш интерфейс взаимодействия с нашей Store моделью
    Создание юзера
    """
    class Meta(UserCreationForm.Meta):
        model = Store
        fields = ('username', 'email')



class StoreChangeForm(UserChangeForm):
    """
    Наш интерфейс взаимодействия с нашей Store моделью
    Редактирование юзера
    """
    class Meta(UserChangeForm.Meta):
        model = Store
        fields =  ('username', 'email') 