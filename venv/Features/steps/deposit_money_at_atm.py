from behave import *

# Background
@given('that the account has UGX "{initial_balance}"')
def account_has_funds(context, initial_balance):
    context.initial_balance = int(initial_balance)

# Background
@given('transaction fee of UGX "{transaction_fees}"')
def transaction_fees(context, transaction_fees):
    context.transaction_fees = int(transaction_fees)

# Background
@given('Account is "{status}"')
def account_is_locked(context, status):
    context.status = str(status)

#successful deposit
