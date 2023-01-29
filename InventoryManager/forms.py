from django import forms
from django.core.exceptions import ValidationError

FormChoices = ["Status Check", "Check In", "Check Out"]


class InOutForm(forms.Form):
    def _UPCLengthValidator(self):
        if len(str(self)) == 9:
            return True
        else:
            raise ValidationError("UPC must be 9 digits")

    def _UPCNumValidator(self):
        if str(self).isnumeric():
            return True
        else:
            raise ValidationError("UPC cannot have letters or special characters")

    UPC = forms.IntegerField(validators=[_UPCLengthValidator, _UPCNumValidator])
    Scan_Type = forms.ChoiceField(choices=[(x, x) for x in FormChoices])

