from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class loan(models.Model):
    current_loan_amount = models.BigIntegerField()
    annual_income = models.BigIntegerField()
    monthly_debt = models.BigIntegerField()
    number_of_open_accounts = models.BigIntegerField()
    maximum_open_credit = models.BigIntegerField()
    term = models.CharField(max_length=30)
    home_ownership = models.CharField(max_length=30)
    bankruptcies = models.IntegerField()
    years_in_current_job = models.CharField(max_length=30)
    pdf_file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.pdf_file.name
    
    
class loanoffers(models.Model):
    type=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    category=models.IntegerField()    

class Creditoffers(models.Model):
    type=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    category=models.IntegerField() 
    
class invest(models.Model):
    occupation=models.CharField(max_length=30)
    time_to_manage=models.IntegerField()
    time_to_reach_goal=models.IntegerField()
    return_of_investment=models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    location=models.CharField(max_length=15) 
    pdf_file = models.FileField(upload_to='pdfs/',null=True,blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def _str_(self):
        return self.pdf_file.name

class FundsOffer(models.Model):
    type=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    category=models.IntegerField() 
    

    