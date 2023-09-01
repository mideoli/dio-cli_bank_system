#!/usr/bin/python3

menu = """
CLI BANK SYSTEM
[1] Deposit
[2] Withdrawal
[3] Extract
[0] Quit

Select an option: """

balance = 0
limit = 500
extract = ""
number_withdrawals = 0
LIMIT_WITHDRAWAL = 3

while True:
    option = int(input(menu))

    if option == 1:
        value = float(input("Enter the amount to deposit: "))

        if value > 0:
            balance += value
            extract += f"Deposit: $ {value:.2f}\n"

        else:
            print("The operation failed! The entered amount is invalid!")
    elif option == 2:
        value = float(input("Enter the amount to withdrawal: "))

        exceeded_balance = value > balance

        exceeded_limit = value > limit

        exceeded_withdrawal = number_withdrawals >= LIMIT_WITHDRAWAL

        if exceeded_balance:
            print("Operation failed! You don't have enough balance.")

        elif exceeded_limit:
            print("Operation failed! The entered amount exceeds the limit.")

        elif exceeded_withdrawal:
            print("Operation failed! Exceeded the number of withdrawals.")

        elif value > 0:
            balance -= value
            print("Withdrawal successful")
            extract += f"Withdrawal: $ {value:.2f}\n"
            number_withdrawals += 1

        else:
            print("Operation failed! The entered amount is invalid.")

    elif option == 3:
        print("\n===== EXTRACT =====")
        print("No moves were made." if not extract else extract)
        print(f"\nBalance: $ {balance:.2f}")
        print("=====================")

    elif option == 0:
        break

else:
    print("Invalid operation, please select the desired operation.")
