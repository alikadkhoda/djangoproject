from django import forms
class searchForm(forms.Form):
    searchText = forms.CharField(max_length=100, label="جستجو", required=False)