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
@when('I deposit UGX {deposit_amount}')
def successful_deposit(context, deposit_amount):
    context.deposit_amount = int(deposit_amount)
    remaining_balance = deposit(context)
    assert remaining_balance == context.initial_balance + (context.deposit_amount - context.transaction_fees)

def deposit(context):
    my_balance = context.initial_balance + (context.deposit_amount - context.transaction_fees)
    return my_balance

#successful deposit
@when('Account state is "{status}"')
def account_state(context, status):
    if status == "unlocked":
        context.successful_deposit = True
    elif status == "locked":
        context.successful_deposit = False

#successful deposit
@then('Feedback reads "Successful"')
def feedback(context):
    assert context.successful_deposit is True


#Failed Deopsit
@when('I fail deposit UGX {deposit_amount}')
def unsuccessful_deposit(context, deposit_amount):
    context.deposit_amount = int(deposit_amount)
    remaining_balance = context.initial_balance
    assert remaining_balance == context.initial_balance 


#unsuccessful deposit
@when('failedAccount state is "{status}"')
def account_state(context, status):
    if status == "unlocked":
        context.unsuccessful_deposit = False
    elif status == "locked":
        context.unsuccessful_deposit = True

@then('failFeedback reads "Unable to transact!"')
def failfeedback(context):
    assert context.unsuccessful_deposit is True
