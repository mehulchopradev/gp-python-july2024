from com.globalpayex.banking.account import Account
from com.globalpayex.banking.min_bal_error import MinBalError

a1 = Account(acc_name='mehul', acc_type='Savings', balance=10000)

try:
  ub = a1.withdraw(amt=9500)
except ValueError:
  print('withdrawl amt must be more than 0')
except MinBalError:
  print('min bal of account not getting maintained')
else:
  print('updated balance is {0}'.format(ub))


ub = a1.deposit(6000)
print('updated balance after deposit is {0}'.format(ub))