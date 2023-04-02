from django.db import models

from .constants import TRANSACTION_TYPE_CHOICES
from accounts.models import UserBankAccount,User


class Transaction(models.Model):
    account = models.ForeignKey(
        UserBankAccount,
        related_name='transactions',
        on_delete=models.CASCADE,
    )
    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    balance_after_transaction = models.DecimalField(
        decimal_places=2,
        max_digits=12
    )
    transaction_type = models.PositiveSmallIntegerField(
        choices=TRANSACTION_TYPE_CHOICES
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.account.account_no)

    class Meta:
        ordering = ['timestamp']


class Loan(models.Model):
    user = models.ForeignKey(
        User,
        related_name='Loan',
        on_delete=models.CASCADE,
    )

    full_Name = models.CharField(max_length=512)
    email = models.CharField(max_length=512)
    birth_date = models.DateTimeField()
    loan_amount = models.CharField(max_length=512)
    loan_purpose =models.CharField(max_length=512)
    loan_emi = models.CharField(max_length=512)
    apply_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
        # .user.email



