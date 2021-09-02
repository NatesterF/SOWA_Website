from django import forms

class NameForm(forms.Form):
    group_name = forms.CharField(label='Group Name', max_length=100)
