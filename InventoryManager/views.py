from django.shortcuts import render
from .forms import InOutForm


# Create your views here.
def index(request):
    #items_by_name = ItemNames.objects.all()
    context = {'lookup_form': InOutForm}
    return render(request, 'InventoryManager/index.html', context)
