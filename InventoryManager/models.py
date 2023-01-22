from django.db import models


# Create your models here.
class ItemNames(models.Model):
    item_name = models.CharField(max_length=250, unique=True)


class TechCategories(models.Model):
    category_name = models.CharField(max_length=250, unique=True)


class Manufacturers(models.Model):
    manufacturer_name = models.CharField(max_length=250, unique=True)


class TechInventory(models.Model):
    total_stock = models.IntegerField()
    category = models.ForeignKey(to=TechCategories, on_delete=models.DO_NOTHING)
    num_available = models.IntegerField()
    item_name = models.ForeignKey(to=ItemNames, on_delete=models.DO_NOTHING)
    manufacturer = models.ForeignKey(to=Manufacturers, on_delete=models.DO_NOTHING)


class Barcodes(models.Model):
    tech_inventory = models.ForeignKey(to=TechInventory, on_delete=models.DO_NOTHING)
    upc = models.IntegerField(unique=True)


class InOutStatus(models.Model):
    checked_in = models.BooleanField(default=True)
    barcode = models.ForeignKey(to=Barcodes, on_delete=models.DO_NOTHING)


class UseDescription(models.Model):
    barcode = models.ForeignKey(to=Barcodes, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=1000)
