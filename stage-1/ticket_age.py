customer_name = input("What is your name? ")
hours_since_opened = float(input("How many hours has the ticket been open? "))
minutes_since_opened = hours_since_opened * 60
days_since_opened = hours_since_opened / 24
print(f"Ticket for {customer_name} has been opened for {minutes_since_opened} minutes, ({days_since_opened} days).")