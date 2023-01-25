from django.shortcuts import render
from .forms import InOutForm
from .models import Barcodes


# Create your views here.
def index(request):
    #items_by_name = ItemNames.objects.all()
    context = {'in_out_form': InOutForm}
    return render(request, 'InventoryManager/index.html', context)


def _GetTechInventoryInfo(upc):
    Barcode_lookup = Barcodes.objects.all().filter(upc=upc)
    if Barcode_lookup:
        # TODO: add in some barcodes as a test
        pass


def lookup(request):
    if request.method == "POST":
        context = {'in_out_form': InOutForm}
        Form = InOutForm(request.POST)
        if Form.is_valid():
            # TODO: lookup barcode, run function to check it in or out, or get data
            context['InfoSubmitted'] = Form.data
            _GetTechInventoryInfo(Form.data.get('UPC'))
            return render(request, 'InventoryManager/index.html', context)
