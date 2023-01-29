from json import dumps

from django.shortcuts import render
from .forms import InOutForm
from .models import Barcodes, TechInventory, UseDescription, ItemStatus


# Create your views here.
def index(request):
    #items_by_name = ItemNames.objects.all()
    context = {'in_out_form': InOutForm}
    return render(request, 'InventoryManager/index.html', context)


def _GetTechInventoryInfo(upc):
    Barcode_lookup = Barcodes.objects.all().filter(upc=upc)
    if Barcode_lookup:
        return Barcode_lookup.values()[0]
    else:
        return None


def _GetStatusCheck(tech_id, upc):
    tech_inv_info = TechInventory.objects.get(pk=tech_id)
    use_desc = UseDescription.objects.get(barcode__upc=upc)
    item_status = ItemStatus.objects.get(barcode__upc=upc)

    final_dict = {
        "Tech Inventory ID": tech_inv_info.id,
        "UPC": upc,
        "Item Name": tech_inv_info.item_name.item_name,
        "Category": tech_inv_info.category.category_name,
        "Manufacturer": tech_inv_info.manufacturer.manufacturer_name,
        "Use Description": use_desc.description,
        "Item Checked In": item_status.checked_in
    }

    print(dumps(final_dict, indent=4))
    return final_dict


def lookup(request):
    if request.method == "POST":
        context = {'in_out_form': InOutForm}
        Form = InOutForm(request.POST)

        if Form.is_valid():
            # lookup barcode, run function to check it in or out, or get data
            context['InfoSubmitted'] = Form.data
            submitted_upc_info = _GetTechInventoryInfo(Form.data.get('UPC'))
            scan_type = Form.data.get('Scan_Type')
            context['SearchAttempted'] = True

            if submitted_upc_info:
                tech_inv_id = submitted_upc_info['tech_inventory_id']
                context['BarcodeMatch'] = submitted_upc_info

                item_status = _GetStatusCheck(tech_inv_id, submitted_upc_info['upc'])
                context['item_status'] = item_status

                if scan_type == "Status Check":
                    pass
                elif scan_type == "Check In" or scan_type == "Check Out":
                    success = _CheckInCheckOut(submitted_upc_info['upc'], scan_type)
                    if success:
                        context['StatusUpdated'] = True
                        item_status = _GetStatusCheck(tech_inv_id, submitted_upc_info['upc'])
                        context['item_status'] = item_status
                    else:
                        context['StatusUpdated'] = False
                        item_status = _GetStatusCheck(tech_inv_id, submitted_upc_info['upc'])
                        context['item_status'] = item_status

            return render(request, 'InventoryManager/index.html', context)
        else:
            print(Form.errors.as_data())
            context['Err'] = Form.errors.as_data()
            return render(request, 'InventoryManager/index.html', context)


def _CheckInCheckOut(upc, scantype):
    current_status = ItemStatus.objects.get(barcode__upc=upc).checked_in
    if not current_status:
        print("item is currently checked out")
        IS = ItemStatus.objects.get(barcode__upc=upc)
        if scantype == "Check In":
            IS.checked_in = True
            IS.save()
            print("Item is now checked in")
            return True
        else:
            print("No change made.")
            return False
    elif current_status:
        print("Item is currently checked in")
        IS = ItemStatus.objects.get(barcode__upc=upc)
        if scantype == "Check Out":
            IS.checked_in = False
            IS.save()
            print("Item is now checked out")
            return True
        else:
            print("No change made.")
            return False
    else:
        print("Item's status is unknown")
