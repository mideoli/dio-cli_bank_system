# Python: CLI Bank System

Banking system with withdrawal, deposit and view statement operations.

## Description of the project
We were hired by a large bank to develop their new system. This bank wants to modernize its operations and for that purpose chose the Python language. For the first version of the system, we should implement only 3 operations: deposit, withdrawal and extract.

### Deposit operation
it must be possible to deposit positive amounts to a bank account. The v1 of the project only works with 1 user, so we don't have to worry about identifying the branch number and bank account. All deposits must be stored in a variable and displayed in the extract operation

### Withdrawal operation
The system should allow 3 daily withdrawals with a maximum limit of $500.00 per withdrawal. If the user does not have a balance in the account, the system should display a message informing that it will not be possible to withdraw the money due to lack of balance. All withdrawals must be stored in a variable and displayed in the statement operation.

### Extract operation
This operation should list all deposits and withdrawals made in the account. At the end of the listing, the current account balance should be displayed. If the extract is blank, display the message: no transactions were carried out.
Values must be displayed using the $xxx.xx format.
