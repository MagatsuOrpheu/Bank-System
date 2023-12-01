# Bank System

### This is the first challenge of the Python Development formation from DIO (DIgital Innovation One)

## This section is the version 1.0 of the bank system
We need to create a bank system using python. For its first version it must have 3 operations: Deposit, Withdraw and Bank Statement.

In this version we will work with just one user.

All deposits must be stored in a variable and be available in the bank statement operation.

The system must only allow 3 daily withdrawals with a limit of just R$500. If the user doesn't have a balance available, a message must be displayed stating that it won't be possible due to lack of balance.

All withdrawals must be stored in a variable and be available in the bank statement operation.

The Statement operation must include all deposits and withdrawals made to the account, and at the end return the current balance of the account.

The format used must be: R$ xxxx.xx

### This section is for the updates of the version 2.0

Modularize the code by creating functions for it. Therefore, each operation will have its individual function.

It'll be necessary to create two new functions: Create_User and create current account and link to the new user.

withdraw must be keyword only; deposit must be positional only; bank statement must be positional and keyword (saldo = positional, extrato = keyword)

Create_user = must store users in list. User must have = name, date of birth, cpf and address.
address = logradouro - bairro - cidade/sigla estado.

Two users can't have the same cpf.

Create current account = accounts must be stored in list. Account have = agency, account number and user. The agency is '0001' 