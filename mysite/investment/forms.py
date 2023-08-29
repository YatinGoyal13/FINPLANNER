from django import forms
from .models import loan,invest
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class loanForm(forms.ModelForm):
    term = forms.ChoiceField(choices=(('Long Term', 'Long Term'), ('Short Term', 'Short Term')))
    years_in_current_job = forms.ChoiceField(choices=(
        ('8 years', '8 years'), ('10+ years', '10+ years'), ('3 years', '3 years'),
        ('5 years', '5 years'), ('< 1 year', '< 1 year'), ('2 years', '2 years'),
        ('4 years', '4 years'), ('9 years', '9 years'), ('7 years', '7 years'),
        ('1 year', '1 year'), ('6 years', '6 years')
    ))
    home_ownership = forms.ChoiceField(choices=(
        ('Home Mortgage', 'Home Mortgage'), ('Own Home', 'Own Home'),
        ('Rent', 'Rent'), ('HaveMortgage', 'HaveMortgage')
    ))
    bankruptcies = forms.ChoiceField(choices=(
        (0, 'NO'), (1, 'YES')
    ))
    class Meta:
        model = loan
        fields = '__all__'

    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get('pdf_file')
        if pdf_file:
            if not pdf_file.name.endswith('.pdf'):
                raise ValidationError('Only PDF files are allowed.')
        return pdf_file
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Upload'))
        
class investForm(forms.ModelForm):
    occupation= forms.ChoiceField(choices=((0, 'Business'), (1, 'Job')))
    location= forms.ChoiceField(choices=((2, 'Metropolitan'), (1, 'Urban'),(0, 'Rural')))
    time_to_manage=forms.ChoiceField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    time_to_reach_goal=forms.ChoiceField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    class Meta:
        model = invest
        fields = '__all__'   
    def clean_pdf_file(self):
        pdf_file = self.cleaned_data.get('pdf_file')
        if pdf_file:
            if not pdf_file.name.endswith('.pdf'):
                raise ValidationError('Only PDF files are allowed.')
        return pdf_file
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Upload'))        