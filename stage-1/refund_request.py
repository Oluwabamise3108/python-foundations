# 1. Ask for an order ID, a refund amount, and a reason for the refund.
order_id = input("Enter the order ID: ")
cleaned_id = order_id.strip().upper()
prefix = "ORD-"
order_number = cleaned_id[len(prefix):]
is_number_valid = order_number.isdigit()

refund_amount = float(input("Enter the refund amount: "))

reason = input("Enter the reason for the refund: ")
valid_reasons = ["damaged", "late", "wrong item"]
cleaned_reason = reason.strip().lower()

# 2. The order ID must start with ORD- and have something after it
if not cleaned_id.startswith(prefix) or cleaned_id == prefix or not is_number_valid:
    print(f"Order ID {cleaned_id} is invalid. Must start with {prefix} and have a valid order number.")

# 3. The reason must be one of: damaged, late, wrong item
elif cleaned_reason not in valid_reasons:
    print(f"Reason '{cleaned_reason}' is invalid. Accepted reasons are: {', '.join(valid_reasons)}.")

# 4. The amount must be greater than 0
elif refund_amount <= 0:
    print(f"Refund amount {refund_amount} is invalid. Must be greater than 0.")

# 5. Amount above 50000 need a manager's approval: say so
elif refund_amount > 50000:
    print(f"Refund amount {refund_amount} requires manager's approval.")

# 6. Otherwise approve, and print the order number, the amount and the reason
else:
    print(f"Refund approved for order {cleaned_id}. Amount: {refund_amount}, Reason: {cleaned_reason}.")