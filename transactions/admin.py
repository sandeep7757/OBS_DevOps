from django.contrib import admin

from transactions.models import Transaction,Loan

admin.site.register(Transaction)

admin.site.register(Loan)

