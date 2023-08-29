from django.contrib import admin

# Register your models here.
from .models import loan,loanoffers,Creditoffers,invest,FundsOffer


admin.site.register(loan)
admin.site.register(loanoffers)
admin.site.register(Creditoffers)
admin.site.register(invest)
admin.site.register(FundsOffer)
