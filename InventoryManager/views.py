from json import dumps

from django.shortcuts import render
from .forms import InOutForm
from .models import Barcodes, TechInventory, UseDescription


# Create your views here.
def index(request):
    #items_by_name = ItemNames.objects.all()
    context = {'in_out_form': InOutForm}
    return render(request, 'InventoryManager/index.html', context)


def _GetTechInventoryInfo(upc):
    Barcode_lookup = Barcodes.objects.all().filter(upc=upc)
    if Barcode_lookup:
        print(Barcode_lookup.values()[0])
        return Barcode_lookup.values()[0]
    else:
        return None


def _GetStatusCheck(tech_id, upc):
    tech_inv_info = TechInventory.objects.get(pk=tech_id)
    use_desc = UseDescription.objects.get(barcode__upc=upc)
    final_dict = {
        "tech_inventory_id": tech_inv_info.id,
        "UPC": upc,
        "item_name": tech_inv_info.item_name.item_name,
        #"total_stock": tech_inv_info.total_stock,
        "category": tech_inv_info.category.category_name,
        "manufacturer": tech_inv_info.manufacturer.manufacturer_name,
        "Use Description": use_desc.description
        #"num_available": tech_inv_info.num_available
    }

    print(dumps(final_dict, indent=4))
    return final_dict


def lookup(request):
    if request.method == "POST":
        context = {'in_out_form': InOutForm}
        Form = InOutForm(request.POST)
        if Form.is_valid():
            # TODO: lookup barcode, run function to check it in or out, or get data
            context['InfoSubmitted'] = Form.data
            # TODO: now lookup item name and CheckIn status.
            submitted_upc_info = _GetTechInventoryInfo(Form.data.get('UPC'))
            tech_inv_id = submitted_upc_info['tech_inventory_id']
            scan_type = Form.data.get('Scan_Type')
            context['SearchAttempted'] = True
            if submitted_upc_info:
                context['BarcodeMatch'] = submitted_upc_info
                if scan_type == "Status Check":
                    item_status = _GetStatusCheck(tech_inv_id, submitted_upc_info['upc'])
                    context['item_status'] = item_status
            return render(request, 'InventoryManager/index.html', context)
