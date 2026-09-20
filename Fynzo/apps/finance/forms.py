from django import forms
from .models import Account, Category, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'account_type', 'balance', 'currency']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-gray-800/50 border border-gray-700 rounded-lg px-4 py-2.5 text-white focus:outline-none focus:border-fynzo-highlight transition-colors'}),
            'account_type': forms.Select(attrs={'class': 'w-full bg-gray-800/50 border border-gray-700 rounded-lg px-4 py-2.5 text-white focus:outline-none focus:border-fynzo-highlight transition-colors appearance-none'}),
            'balance': forms.NumberInput(attrs={'class': 'w-full bg-gray-800/50 border border-gray-700 rounded-lg px-4 py-2.5 text-white focus:outline-none focus:border-fynzo-highlight transition-colors', 'step': '0.01'}),
            'currency': forms.TextInput(attrs={'class': 'w-full bg-gray-800/50 border border-gray-700 rounded-lg px-4 py-2.5 text-white focus:outline-none focus:border-fynzo-highlight transition-colors'}),
        }
