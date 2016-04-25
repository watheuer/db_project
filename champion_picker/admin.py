from django.contrib import admin
from import_export.admin import ImportExportMixin, ExportMixin
from import_export import resources
from champion_picker.models import *

class ChampionResource(resources.ModelResource):
    class Meta:
        model = Champion
        import_id_fields = ['name',]

class ChampionAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ['name']
    resource_class = ChampionResource
    class Meta:
        model = Champion

class RoleAdmin(ImportExportMixin, admin.ModelAdmin):
    class Meta:
        model = Role

class WinRateAdmin(ImportExportMixin, admin.ModelAdmin):
    search_fields = ['role1__champion__name']
    class Meta:
        model = WinRate

class ItemAdmin(ImportExportMixin, admin.ModelAdmin):
    class Meta:
        model = Item

class ItemBuildAdmin(ImportExportMixin, admin.ModelAdmin):
    class Meta:
        model = ItemBuild

# Register your models here.
admin.site.register(Champion, ChampionAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(WinRate, WinRateAdmin)
admin.site.register(ItemBuild, ItemBuildAdmin)
admin.site.register(Item, ItemAdmin)
