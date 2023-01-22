from django.contrib import admin
from .models import ItemNames, Barcodes, TechCategories, TechInventory, Manufacturers, InOutStatus, UseDescription

# Register your models here.
admin.site.register(ItemNames)
admin.site.register(Barcodes)
admin.site.register(TechCategories)
admin.site.register(TechInventory)
admin.site.register(Manufacturers)
admin.site.register(InOutStatus)
admin.site.register(UseDescription)
