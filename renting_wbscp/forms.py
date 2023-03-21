from django import forms
from renting_wbscp.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'age', 'phone_number', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }

