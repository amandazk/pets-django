from django.contrib import admin
from .models import Pet

# Register your models here.
#admin.site.register(Pet)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'cidade', 'descricao', 'user']
