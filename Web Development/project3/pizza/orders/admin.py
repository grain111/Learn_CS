from django.contrib import admin
from .models import Group, ExtraIngridient, MenuItem, MenuCombination


class MenuCombinationInline(admin.TabularInline):
    model = MenuCombination
    extra = 1

class MenuItemAdmin(admin.ModelAdmin):
    inlines = (MenuCombinationInline, )

class ExtraIngridientAdmin(admin.ModelAdmin):
    inlines = (MenuCombinationInline, )

admin.site.register(Group)
admin.site.register(ExtraIngridient, ExtraIngridientAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
# admin.site.register(MenuCombination)
