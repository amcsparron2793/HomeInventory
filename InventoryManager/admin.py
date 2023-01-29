from django.contrib import admin
from .models import ItemNames, Barcodes, TechCategories, TechInventory, Manufacturers, ItemStatus, UseDescription
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# TODO: make this work to enter info easier


class ItemNamesResource(resources.ModelResource):
    class Meta:
        model = ItemNames
        skip_unchanged = True
        report_skipped = True


class ItemNamesAdmin(ImportExportModelAdmin):
    resource_class = ItemNamesResource
    list_display = ('id', 'item_name')
    #inlines = [ItemNamesInline]


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

# TODO: import barcodes, tech inventory, item status use description?


# Register your models here.
admin.site.register(ItemNames, ItemNamesAdmin)
admin.site.register(Barcodes)
admin.site.register(TechCategories, TechCategoriesAdmin)
admin.site.register(TechInventory)
admin.site.register(Manufacturers, ManufacturersAdmin)
admin.site.register(ItemStatus)
admin.site.register(UseDescription)
