from django import forms


class StudentSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')  #디자인 말고 규격만
