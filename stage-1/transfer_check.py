# 1. Fixed account balance with two decimal places in a variable at the top: 50000.
account_balance = 50000.00

# 2. Ask for a destination account number, a currency, and an amount.
destination_account = input("Enter the destination account number: ").strip()
currency = input("Enter the currency (NGN/USD): ").strip().upper()
amount = float(input("Enter the amount to transfer: "))

# 3. The account number must be exactly 10 characters, all digits.
if len(destination_account) != 10 or not destination_account.isdigit():
    print("Invalid destination account number. Must be exactly 10 digits.")

# 4. The currency must be NGN or USD, typed in any case.
elif currency not in ["NGN", "USD"]:
    print("Invalid currency. Must be either NGN or USD.")

# 5. The amount must be greater than 0.
elif amount <= 0:
    print("Invalid amount. Must be greater than 0.")

# 6. The amount mustn't exceed the balance.
elif amount > account_balance:
    print(f"Insufficient funds. Your balance is {account_balance:.2f}.")

# 7. On success, print the transfer details and the balance remaining.
else:
    account_balance -= amount
    print(f"Transfer successful! {amount:.2f} {currency} has been sent to account {destination_account}.")
    print(f"Remaining balance: {account_balance:.2f} {currency}.")