Feature: Withdraw Transactions at the ATM

  As a Bank Manager, I want to ensure that the integrity of the Account 
  balances remains intact though I charge for every transaction, whether
  successfull or not until down to minimum account balance.

  Background: Setting Account transaction conditions
    Given that account balance is UGX 100000
    Given withdrawal fees of UGX 5000
    And maintaining a minimum balance of UGX 20000

    @WithdrawalsIntegrityCheck
    Scenario Outline: Ensuring integrity of withdrawals
      When I withdraw amount UGX "<withdrawAmount>"
      Then Account balance becomes UGX "<newBalance>"

    Examples:
      | withdrawAmount | newBalance |
      | 55000          | 40000      |
      | 110000         | 95000      |
      | 80000          | 95000      |

