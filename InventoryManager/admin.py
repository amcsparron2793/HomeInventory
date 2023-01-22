from django.contrib import admin
from .models import ItemNames, Barcodes, TechCategories, TechInventory, Manufacturers, ItemStatus, UseDescription

# Register your models here.
admin.site.register(ItemNames)
admin.site.register(Barcodes)
admin.site.register(TechCategories)
admin.site.register(TechInventory)
admin.site.register(Manufacturers)
admin.site.register(ItemStatus)
admin.site.register(UseDescription)
