from django.contrib import admin
from .models import ItemNames, Barcodes, TechCategories, TechInventory, Manufacturers, ItemStatus, UseDescription
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class ItemNamesResource(resources.ModelResource):
    class Meta:
        model = ItemNames
        skip_unchanged = True
        report_skipped = True


class ItemNamesAdmin(ImportExportModelAdmin):
    resource_class = ItemNamesResource
    list_display = ('id', 'item_name')


class ManufacturersResource(resources.ModelResource):
    class Meta:
        model = Manufacturers
        skip_unchanged = True
        report_skipped = True


class ManufacturersAdmin(ImportExportModelAdmin):
    resource_class = ManufacturersResource
    list_display = ('id', 'manufacturer_name')


class TechCategoriesResource(resources.ModelResource):
    class Meta:
        model = TechCategories
        skip_unchanged = True
        report_skipped = True


class TechCategoriesAdmin(ImportExportModelAdmin):
    resource_class = TechCategoriesResource
    list_display = ('id', 'category_name')


class TechInventoryResource(resources.ModelResource):
    class Meta:
        model = TechInventory
        skip_unchanged = True
        report_skipped = True


# noinspection PyMethodMayBeStatic
class TechInventoryAdmin(ImportExportModelAdmin):
    resource_class = TechInventoryResource
    list_display = ['id', 'item_name', 'category', 'manufacturer', 'total_stock',
                    'num_available', 'Barcodes_Assigned']
    list_display_links = ['id', 'item_name', 'category', 'manufacturer']

    def Barcodes_Assigned(self, obj):
        return Barcodes.objects.filter(tech_inventory_id=obj.id).count()


class BarcodesAdmin(admin.ModelAdmin):
    list_display = ['tech_inventory', 'upc']


class ItemStatusAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'checked_in']


class UseDescriptionAdmin(admin.ModelAdmin):
    list_display = ['barcode', 'description']


# Register your models here.
admin.site.register(ItemNames, ItemNamesAdmin)
admin.site.register(TechCategories, TechCategoriesAdmin)
admin.site.register(TechInventory, TechInventoryAdmin)
admin.site.register(Manufacturers, ManufacturersAdmin)

admin.site.register(Barcodes, BarcodesAdmin)
admin.site.register(ItemStatus, ItemStatusAdmin)
admin.site.register(UseDescription, UseDescriptionAdmin)
