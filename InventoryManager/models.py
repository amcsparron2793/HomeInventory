from django.db import models


# Create your models here.
class ItemNames(models.Model):
    item_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name_plural = "Item Names"


class TechCategories(models.Model):
    category_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = "Tech Categories"


class Manufacturers(models.Model):
    manufacturer_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        verbose_name_plural = "Manufacturers"


class TechInventory(models.Model):
    total_stock = models.IntegerField()
    category = models.ForeignKey(to=TechCategories, on_delete=models.DO_NOTHING)
    num_available = models.IntegerField()
    item_name = models.ForeignKey(to=ItemNames, on_delete=models.DO_NOTHING)
    manufacturer = models.ForeignKey(to=Manufacturers, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str((self.id, self.item_name))

    class Meta:
        verbose_name_plural = "Tech Inventory"


class Barcodes(models.Model):
    tech_inventory = models.ForeignKey(to=TechInventory, on_delete=models.DO_NOTHING)
    upc = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.upc)

    class Meta:
        verbose_name_plural = "Barcodes"


class ItemStatus(models.Model):
    checked_in = models.BooleanField(default=True)
    barcode = models.ForeignKey(to=Barcodes, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Item Statuses"

    def __str__(self):
        return str(self.barcode)


class UseDescription(models.Model):
    barcode = models.ForeignKey(to=Barcodes, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.barcode)
