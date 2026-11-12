ticket_id = input("Enter the ticket ID: ")
priority = input("What is the ticket priority? ")
cleaned = priority.strip().lower()

if ticket_id.startswith("TCK-0") or ticket_id.startswith("tck-0") or ticket_id.startswith(" TCK-0") and cleaned in ["high", "medium", "low"]:
    print(f"Ticket {ticket_id[-5:]} is valid with priority {cleaned}.")
    if cleaned == "high":
        target = "1 hour"
    elif cleaned == "medium":
        target = "4 hours"
    elif cleaned == "low":
        target = "24 hours"
    else:
        target = "Please provide a valid priority."
    print(f"Response target: {target}")
elif ticket_id.startswith("TCK-0") or ticket_id.startswith("tck-0") or ticket_id.startswith(" TCK-0") and cleaned not in ["high", "medium", "low"]:
    print(f"Ticket {ticket_id} has an invalid priority.")
elif ticket_id.startswith("TCK-") or ticket_id.startswith("TCK- ") or ticket_id.startswith("tck- ") or ticket_id.startswith("tck-") and cleaned in ["high", "medium", "low"]:
    print(f"Ticket ID {ticket_id} is incomplete. Please provide the full ticket ID.")
else:
    print(f"Ticket {ticket_id} is invalid.")