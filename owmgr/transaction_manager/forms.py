from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm
from .models import *

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
    due = forms.DateField(widget=DateInput())
