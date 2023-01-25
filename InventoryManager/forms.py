from django import forms

FormChoices = ["Check In", "Check Out", "Status Check"]


class InOutForm(forms.Form):
    UPC = forms.IntegerField()
    Scan_Type = forms.ChoiceField(choices=[(x, x) for x in FormChoices])

