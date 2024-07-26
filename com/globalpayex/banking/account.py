'''
Create Account class
Every Account object will have attributes
  - acc_name
  - acc_type
  - balance
On every Account object we can call following instance methods
  - withdraw(amt) --> updated balance
  - deposit(amt) --> updated balance
'''
from com.globalpayex.banking.min_bal_error import MinBalError
from com.globalpayex.banking.utils import cannot_withdraw
class Account:

  min_balance = 1000

  def __init__(self, acc_name, acc_type, balance):
    self.acc_name = acc_name
    self.acc_type = acc_type
    self.balance = balance

  def deposit(self, amt):
    self.balance += amt
    return self.balance
  
  def withdraw(self, amt):
    if amt <= 0:
      raise ValueError('withdrawl amt must be more than 0')
    
    if cannot_withdraw(account=self, amt=amt):
      raise MinBalError(msg='min bal of account not getting maintained')
    
    self.balance -= amt
    return self.balance