from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    PAYMENT_CHOICES = [
        ('cod', 'Cash on Delivery'),
        ('online', 'Online Payment'),
    ]

    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Order

        fields = [
            'first_name',
            'last_name',
            'email',
            'address',
            'city',
            'payment_method',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name'
            }),

            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address'
            }),

            'address': forms.TextInput(attrs={
                'placeholder': 'Address'
            }),

            'city': forms.TextInput(attrs={
                'placeholder': 'City'
            }),
        }