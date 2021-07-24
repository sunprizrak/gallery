from django.contrib import admin
from .models import Virtual


@admin.register(Virtual)
class VirtualAdmin(admin.ModelAdmin):
    list_display = ('title', 'field_name_log', 'field_name_nolog', 'slug')
    prepopulated_fields = {'slug': ('title',)}