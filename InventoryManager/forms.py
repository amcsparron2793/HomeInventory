from django import forms

FormChoices = (("Check In", "Check In"), ("Check Out", "Check Out"), ("Status Check", "Status Check"))


class InOutForm(forms.Form):
    UPC = forms.IntegerField()
    Scan_Type = forms.ChoiceField(choices=FormChoices)

