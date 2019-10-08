from django.contrib import admin

from .models import Menu

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    filter_horizontal = ("menu", )

class CustomerAdmin(admin.ModelAdmin):
    filter_horizontal = ("customer", )

class CartAdmin(admin.ModelAdmin):
    filter_horizontal = ("cart", )


admin.site.register(Menu)
