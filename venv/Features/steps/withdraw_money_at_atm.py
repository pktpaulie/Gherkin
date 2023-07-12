from behave import *

# Background
@given('that account has UGX "{initial_balance}"')
def account_has_funds(context, initial_balance):
    context.initial_balance = int(initial_balance)

# Background
@given('transaction fees of UGX "{transaction_fees}"')
def transaction_fees(context, transaction_fees):
    context.transaction_fees = int(transaction_fees)

# Background
@given('maintaining minimum balance of UGX "{min_balance}"')
def minimum_balance(context, min_balance):
    context.min_balance = int(min_balance)

# Successful withdrawal
@when('I withdraw UGX {amount}')
def successful_withdrawal(context, amount):
    context.withdraw = int(amount)
    remaining = withdraw(context)
    assert remaining == context.initial_balance - (context.withdraw + context.transaction_fees)

def withdraw(context):
    initial_balance = context.initial_balance - (context.withdraw + context.transaction_fees)
    return initial_balance


@then('Account balance is {balance}')
def account_balance_after_withdrawal(context, balance):
    context.balance = int(balance)
    assert context.balance == context.initial_balance - (context.withdraw + context.transaction_fees)


#failed withdrawal
@when('I fail withdraw UGX {withdraw_amount}')
def failed_withdraw(context, withdraw_amount):
    context.withdraw = int(withdraw_amount)
    if context.withdraw >= context.min_balance:
        context.failed_transaction = True
    else:
        context.failed_transaction = False

@then('failed Account balance is {initial_balance}')
def failed_withdrawal(context, initial_balance):
    context.balance = int(initial_balance)
    assert context.balance == context.initial_balance
