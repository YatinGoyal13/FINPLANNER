from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from user.models import Profile
from phonenumber_field.formfields import PhoneNumberField
from .widgets import DatePicker


class ProfileCreationForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput)
    username = forms.CharField(widget=forms.TextInput)
    name = forms.CharField(widget=forms.TextInput)
    phone = PhoneNumberField(region='IN')
    registered_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    state = forms.CharField(widget=forms.Select(choices=[]))
    district = forms.CharField(widget=forms.Select(choices=[]))
    dob=forms.DateField(widget=DatePicker())

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)
        self.fields['state'].widget.attrs['onchange'] = 'updateDistricts()'
        
        for field_name, field in self.fields.items():
            field.required = True

    class Meta:
        model = Profile
        fields = ['username', 'email','name','phone','dob','state','district', 'password1', 'password2']


class AccountUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(region='IN', widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))

    class Meta:
        model = Profile
        fields = ['email', 'username','phone']

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Profile.objects.exclude(pk=self.instance.pk).get(email=email)
            except Profile.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email) 
        
