from django.contrib import admin

from user.models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    """
    Пользовательский интерфейс администрирования для администратора.
    """
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff',
                    'is_superuser')
