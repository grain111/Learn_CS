from django.contrib import admin
from .models import Group, ExtraIngridient, MenuItem, MenuCombination

admin.site.register(Group)
admin.site.register(ExtraIngridient)
admin.site.register(MenuItem)
admin.site.register(MenuCombination)
