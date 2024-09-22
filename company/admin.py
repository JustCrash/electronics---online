from django.contrib import admin

from company.models import Supplier, Company


def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


clear_debt.short_description = "Очистить задолженность"

fields_display = [
    'name_supplier',
    'debt',
    'company_customer',
    'company_supplier',
    'owner',
]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Интерфейс администратора для поставщика.
    """
    list_display = fields_display
    actions = [clear_debt]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """
    Интерфейс администрирования компании для администратора.
    """
    list_display = ('id', 'name', 'email', 'country', 'city', 'type_company', 'number_home', 'street',
                    'owner')
    search_fields = ('city',)
    list_filter = ("city",)
