DEPOSIT = 1
WITHDRAWAL = 2
INTEREST = 3

TRANSACTION_TYPE_CHOICES = (
    (DEPOSIT, 'Deposit'),
    (WITHDRAWAL, 'Withdrawal'),
    (INTEREST, 'Interest'),
)

EDLoan = 'EDL'
HomeLoan = 'HF'
CarLoan = 'CL'
MaritalLoan = 'ML'
GoldLoan ='GL'
Others= 'O'
Three = '3'
Six='6'
Nine ='9'
Twelve='12'
Eighteen= '18'
twenty4 ='24'
thirty6 = '36'


LOAN_PURPOSE = (
    (EDLoan, "Education Loan"),
    (HomeLoan, "Home Loan"),
    (CarLoan,"Car Loan"),
    (MaritalLoan,'Marital Loan'),
    (GoldLoan,'Gold Loan'),
    (Others,"Others"),
)
LOAN_EMI = (
    (Three, "3 months"),
    (Six, "6 months"),
    (Nine,"9 months"),
    (Twelve,'12 months'),
    (Eighteen,'18 months'),
    (twenty4,'24 months'),
    (thirty6,'36 months'),
)