ticket_id = input("Enter the ticket ID: ")
prefix = "TCK-"
priority = input("What is the ticket priority? ")
cleaned = priority.strip().lower()

if ticket_id.startswith(prefix) and cleaned == "high" or cleaned == "medium" or cleaned == "low":
    if cleaned == "high":
        target = "1 hour"
    elif cleaned == "medium":
        target = "4 hours"
    elif cleaned == "low":
        target = "24 hours"
    else:
        target = "Please provide a valid priority. Accepted values are high, medium, or low."
    print(f"Response target: {target}")

elif ticket_id.startswith(prefix) and cleaned not in ["high", "medium", "low"]:
    print(f"Ticket {ticket_id} has an invalid priority.")
elif ticket_id.startswith(prefix) and cleaned in ["high", "medium", "low"]:
    print(f"Ticket ID {ticket_id} is incomplete. Please provide the full ticket ID.")
else:
    print(f"Ticket {ticket_id} is invalid. Must start with {prefix}.")
