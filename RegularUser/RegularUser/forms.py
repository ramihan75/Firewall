from .models import RegularUser

# Заготовки интерфейса пользовательской модели
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegularUserCreationForm(UserCreationForm):
    """
    Наш интерфейс взаимодействия с нашей RegularUser моделью
    Создание юзера
    """
    class Meta(UserCreationForm.Meta):
        model = RegularUser
        fields = ('username', 'sex', 'age', 'phone_number', 'postal_code')
        

class RegularUserChangeForm(UserChangeForm):
    """
    Наш интерфейс взаимодействия с нашей RegularUser моделью
    Редактирование юзера
    """
    class Meta(UserChangeForm.Meta):
        model = RegularUser
        fields = ('username', 'sex', 'age', 'phone_number', 'postal_code')
