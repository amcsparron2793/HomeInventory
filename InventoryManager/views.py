from django.shortcuts import render
from .models import ItemNames


# Create your views here.
def index(request):
    items_by_name = ItemNames.objects.all()
    context = {'items': items_by_name}
    return render(request, 'InventoryManager/index.html', context)