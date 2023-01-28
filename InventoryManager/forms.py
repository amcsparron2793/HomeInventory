from django import forms

FormChoices = ["Status Check", "Check In", "Check Out"]


class InOutForm(forms.Form):
    UPC = forms.IntegerField()
    Scan_Type = forms.ChoiceField(choices=[(x, x) for x in FormChoices])

