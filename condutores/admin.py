from django.contrib import admin
from .models import Condutor

# Register your models here.
@admin.register(Condutor)
class CondutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'empresa', 'filial')
    search_fields = ('nome', 'empresa', 'filial')