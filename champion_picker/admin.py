from django.contrib import admin
from import_export.admin import ImportExportMixin, ExportMixin
from champion_picker.models import *

class ChampionAdmin(ImportExportMixin, admin.ModelAdmin):
    class Meta:
        model = Champion

# Register your models here.
admin.site.register(Champion, ChampionAdmin)
admin.site.register(Role)
admin.site.register(WinRate)
admin.site.register(ItemBuild)
admin.site.register(Item)
