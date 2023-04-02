from dateutil.relativedelta import relativedelta
from django.shortcuts import HttpResponseRedirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView,TemplateView,RedirectView

from transactions.constants import DEPOSIT, WITHDRAWAL
from transactions.forms import (
    DepositForm,
    TransactionDateRangeForm,
    WithdrawForm,UserLoanCreation
)
from transactions.models import Transaction, Loan

class TransactionRepostView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    form_data = {}

    def get(self, request, *args, **kwargs):
        form = TransactionDateRangeForm(request.GET or None)
        if form.is_valid():
            self.form_data = form.cleaned_data

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )

        daterange = self.form_data.get("daterange")

        if daterange:
            queryset = queryset.filter(timestamp__date__range=daterange)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account,
            'form': TransactionDateRangeForm(self.request.GET or None)
        })

        return context

class TransactionHomeView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_home.html'
    model = Transaction
    form_data = {}

    def get(self, request, *args, **kwargs):
        form = TransactionDateRangeForm(request.GET or None)
        if form.is_valid():
            self.form_data = form.cleaned_data

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )

        daterange = self.form_data.get("daterange")

        if daterange:
            queryset = queryset.filter(timestamp__date__range=daterange)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account,
            'form': TransactionDateRangeForm(self.request.GET or None)
        })

        return context

class LoanRepostView(LoginRequiredMixin, ListView):
    template_name = 'loans/loan_report.html'
    model = Loan
    form_data = {}


    def get_queryset(self):
        queryset = super().get_queryset().filter(
            user=self.request.user
        )

        # daterange = self.form_data.get("daterange")

        # if daterange:
        #     queryset = queryset.filter(timestamp__date__range=daterange)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transactions:transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit Money to Your Account'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        if not account.initial_deposit_date:
            now = timezone.now()
            next_interest_month = int(
                12 / account.account_type.interest_calculation_per_year
            )
            account.initial_deposit_date = now
            account.interest_start_date = (
                now + relativedelta(
                    months=+next_interest_month
                )
            )

        account.balance += amount
        account.save(
            update_fields=[
                'initial_deposit_date',
                'balance',
                'interest_start_date'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money from Your Account'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')

        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )

        return super().form_valid(form)
        
class loadloantemplate(TemplateView):
     template_name = 'loans/loanCreation.html'
     model= Loan

     def post(self, request, *args, **kwargs):
        loan_form = UserLoanCreation(self.request.POST)
        print("hello",self.request.POST.get('full_Name'))
        l = Loan(user = request.user, full_Name=self.request.POST.get('full_Name'),email=self.request.POST.get('email'),birth_date=self.request.POST.get('birth_date'),loan_amount=self.request.POST.get('loan_amount'),loan_purpose=self.request.POST.get('loan_purpose'),loan_emi=self.request.POST.get('loan_emi'))
        l.save()

        if loan_form.is_valid():

            # user = loan_form.save()
    

            messages.success(
                self.request,
                (
                    # f'Thank You For Creating A Bank Account in Online Banking System. '
                    f'"Thank you for submitting your loan application. We have received your request and our team will review it as soon as possible. You can expect to hear back from us within the next few business days regarding the status of your application. If we require any additional information, we will contact you directly. Thank you for choosing our banking services."'
                )
            )
        

        return self.render_to_response(
            self.get_context_data(
                loan_form=loan_form,
            )
        )

     def get_context_data(self, **kwargs):
        if 'loan_form' not in kwargs:
            kwargs['loan_form'] = UserLoanCreation()
        

        return super().get_context_data(**kwargs)



class LoanCreationView(loadloantemplate):

    def loanCreation():
        return

   