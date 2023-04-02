from django.urls import path
from . import views
from .views import DepositMoneyView, WithdrawMoneyView, TransactionRepostView,LoanCreationView,LoanRepostView,TransactionHomeView


app_name = 'transactions'


urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("home/", TransactionHomeView.as_view(), name="transaction_home"),
    path("report/", TransactionRepostView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("loanCreation/", LoanCreationView.as_view(), name="loan_creation"),
    path("loanreport/", LoanRepostView.as_view(), name="loan_report"),
    
]
