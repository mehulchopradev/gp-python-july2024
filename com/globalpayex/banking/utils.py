def cannot_withdraw(account, amt):
  min_balance = 10 if account.acc_type == 'Savings' else 500
  return account.balance - amt < min_balance