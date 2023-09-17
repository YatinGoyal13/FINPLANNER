from django.shortcuts import render, redirect
from .forms import loanForm,investForm
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from joblib import load
import pandas as pd
from .models import loanoffers,Creditoffers,FundsOffer
from user.models import Profile
from django.db.models import ExpressionWrapper, F
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay, Now
from datetime import datetime
pipeline=load('/Users/yatingoyal/Desktop/FINPLANNER/mysite/savedmodels/pipeline.joblib')
pipeline2=load('/Users/yatingoyal/Desktop/FINPLANNER/mysite/savedmodels2/pipeline2.joblib')



@login_required
def loanreq(request):
    if request.method == 'POST':
        form = loanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            CurrentLoanAmount=form.cleaned_data.get('current_loan_amount')
            Term=form.cleaned_data.get('term')
            AnnualIncome=form.cleaned_data.get('annual_income')
            Yearsjob=form.cleaned_data.get('years_in_current_job')
            HomeOwnership=form.cleaned_data.get('home_ownership')
            MonthlyDebt=form.cleaned_data.get('monthly_debt')
            NumberAccounts=form.cleaned_data.get('number_of_open_accounts')
            MaxCredit=form.cleaned_data.get('maximum_open_credit')
            Bankruptcies=form.cleaned_data.get('bankruptcies')
            input_data = pd.DataFrame([[CurrentLoanAmount, Term, AnnualIncome, Yearsjob, HomeOwnership, MonthlyDebt, NumberAccounts, MaxCredit, Bankruptcies]],
                                      columns=['CurrentLoanAmount', 'Term', 'Annual Income', 'Years in current job', 'Home Ownership', 'Monthly Debt', 'Number of Open Accounts', 'Maximum Open Credit', 'Bankruptcies'])

            y_pred = pipeline.predict(input_data)
            score=y_pred[0,0]
            # take fields for ML model from here for ref check user/views.py
            if score>=750:
                cate=1
            elif 650<=score<750:
                cate=2
            elif 550<=score<650:
                cate=3
            else:
                cate=4        
            
            
            filtered_data1 = loanoffers.objects.all()  
            filtered_data2 = Creditoffers.objects.all() 
            
            filtered_data1=filtered_data1.filter(category=cate) 
            filtered_data2=filtered_data2.filter(category=cate) 
            context = {
               'filter_data1': filtered_data1,
               'filter_data2': filtered_data2
            }
            
            messages.success(request, f'File Uploaded Successfully.')
            
            return render(request,'investment/loanoffers.html',context)
    else:
        form = loanForm()
    return render(request, 'investment/upload.html', {'form': form})


@login_required
def investreq(request):
    if request.method == 'POST':
        form = investForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            def scale_value(value, old_min, old_max, new_min, new_max):
                scaled_value = ((value - old_min) / (old_max - old_min)) * (new_max - new_min) + new_min
                return scaled_value
            
            age = random.uniform(18,90)
            fund=random.uniform(10000,1000000)
            fund1 = scale_value(fund, 10000, 1000000, 1, 5)
            certain=form.cleaned_data.get('occupation')
            def map_age_to_risk(age):
                if 18 <= age <= 28:
                    return 5
                elif 29 <= age <= 35:
                    return 4
                elif 36 <= age <= 50:
                    return 3
                elif 51 <= age <= 60:
                    return 2
                else:
                    return 1
            risk= map_age_to_risk(age)
            manage=form.cleaned_data.get('time_to_manage')
            goal=form.cleaned_data.get('time_to_reach_goal')
            location=form.cleaned_data.get('location')
            roi=form.cleaned_data.get('return_of_investment')
            
            
            input_data = pd.DataFrame([[fund1, certain, risk, manage, goal, location, roi]],
                                      columns=['fund_avail','fund_certain','risks', 'time_to_manage', 'time_goal',  'location',  'roi'])
            print(input_data)
            y_pred = pipeline2.predict(input_data)
            score=y_pred[0]
            def map_score_to_category(score):
                if score < 0.15:
                    return 1
                elif 0.15 <= score < 0.20:
                    return 2
                elif 0.20 <= score < 0.25:
                    return 3
                elif 0.25 <= score < 0.30:
                    return 4
                elif 0.30 <= score < 0.35:
                    return 5
                elif 0.35 <= score < 0.40:
                    return 6
                elif 0.40 <= score < 0.45:
                    return 7
                else:
                    return 8
                
            filtered_data3 = FundsOffer.objects.all() 
            filtered_data3=filtered_data3.filter(category=map_score_to_category(score))
            context = {
               'filter_data3': filtered_data3
            }
             
            
            messages.success(request, f'Submitted Successfully.')
            return render(request,'investment/funds.html',context)
    else:
        form = investForm()
    return render(request, 'investment/invest.html',{'form': form})