from behave import *

@given('that account balance is UGX {initial_balance}')
def set_account_balance(context, initial_balance):
    context.account_balance = int(initial_balance)

@given('withdrawal fees of UGX {withdrawal_fees}')
def set_withdrawal_fees(context, withdrawal_fees):
    context.withdrawal_fees = int(withdrawal_fees)

@given('maintaining a minimum balance of UGX {minimum_balance}')
def set_minimum_balance(context, minimum_balance):
    context.minimum_balance = int(minimum_balance)

    
@when('I withdraw amount UGX "{withdraw_amount}"')
def withdraw_amount(context, withdraw_amount):
    context.withdraw_amount = int(withdraw_amount)
    context.new_balance = context.account_balance - (context.withdraw_amount + context.withdrawal_fees)
    if context.new_balance < context.minimum_balance:
        context.new_balance = context.minimum_balance

@then('Account balance becomes UGX "{new_balance}"')
def verify_new_balance(context, new_balance):
    assert context.new_balance == int(context.new_balance)
