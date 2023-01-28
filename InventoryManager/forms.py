from django import forms
from django.core.exceptions import ValidationError
FormChoices = ["Status Check", "Check In", "Check Out"]


class InOutForm(forms.Form):
    def _UPC_Validator(self):
        if len(str(self)) == 9:
            return True
        else:
            raise ValidationError("UPC must be 9 characters")

    UPC = forms.IntegerField(validators=[_UPC_Validator])
    Scan_Type = forms.ChoiceField(choices=[(x, x) for x in FormChoices])

