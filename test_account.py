from com.globalpayex.banking.account import Account
from com.globalpayex.banking.min_bal_error import MinBalError
import pytest

class TestAccount:

  def test_withdraw_valueerror(self):
    amt = 0
    account = Account(acc_name='mehul', acc_type='Savings', balance=10000)

    with pytest.raises(ValueError):
      account.withdraw(amt)

  def test_withdraw_minbalerror(self, monkeypatch):
    def dummy_cannot_withdraw(account, amt):
      return True
    monkeypatch.setattr('com.globalpayex.banking.account.cannot_withdraw', dummy_cannot_withdraw)

    amt = 9500
    account = Account(acc_name='mehul', acc_type='Savings', balance=10000)

    with pytest.raises(MinBalError):
      account.withdraw(amt)