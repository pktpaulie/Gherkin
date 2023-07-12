Feature: Transact money at ATM

  As a Bank Owner, I want to increase my Clients interactions
  with their accounts by introducing ATMs

  Rule: Withdraw money and Deposit money

    Background: Setting Account transaction conditions
      Given that account has UGX "100000"
      And transaction fees of UGX "5000"
      But maintaining minimum balance of UGX "20000"

    @Withdraw @Success
    Scenario: Successful withdrawal
      When I withdraw UGX 50000
      Then Account balance is 45000

    @Withdraw @Failure
    Scenario: Failed withdrawal
      When I fail withdraw UGX 80000
      Then failed Account balance is 100000
