Feature: Transact money at ATM

  As a Bank Owner, I want to increase my Clients interactions
  with their accounts by introducing ATMs

  Rule: Deposit money

    Background: Set Account Deposit conditions
      Given that the account has UGX "50000"
      And transaction fee of UGX "2500"
      But Account is "unlocked"

    @Deposit  @Success
    Scenario: Successful deposit
      When I deposit UGX 50000 
      And Account state is "unlocked"
      Then Feedback reads "Successful"
    
    @Deposit @Failure
    Scenario: Failed deposit
      When I deposit UGX 40000
      And Account state is "locked"
      Then Feedback reads "Unable to transact!"


