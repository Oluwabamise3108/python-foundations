# 1. Ask for the ticket ID and priority.
ticket_id = input("Enter the ticket ID: ")
priority = input("What is the ticket priority? ")

# 2. Clean the ID: remove outer spaces and make it uppercase. Store it in a new variable.
cleaned_id = ticket_id.strip().upper()
prefix = "TCK-"
suffix = cleaned_id[len(prefix):]
is_number_valid = suffix.isdigit()   # Extract the part after the prefix and check if it's all digits
  
    
# 3. Clean the priority.
cleaned_priority = priority.strip().lower()

# 4. If the cleaned ID does not start with the prefix: say it is invalid.
if not cleaned_id.startswith(prefix):
    print(f"Ticket {cleaned_id} is invalid. Must start with {prefix}.")

# 5. Otherwise, if nothing follows the prefix: say it is incomplete.
elif cleaned_id == prefix:
    print(f"Ticket ID {cleaned_id} is incomplete. Please provide the full ticket ID.")

# 6. otherwise, if the suffix is not all digits: say it is invalid.
elif not is_number_valid:
    print(f"Ticket {cleaned_id} has an invalid ID format. Please provide a valid ticket ID.")

# 7. Otherwise, if the priority is not one of the three: say so and list the accepted values.
elif cleaned_priority not in ["low", "medium", "high"]:
    print(f"Ticket {cleaned_id} has an invalid priority. Accepted values are high, medium, or low.")

# 8. Otherwise everything is valid: work out the target, print the number part and the target.      
else:
    if cleaned_priority == "high":
        target = "1 hour"
    elif cleaned_priority == "medium":
        target = "4 hours"
    elif cleaned_priority == "low":
        target = "24 hours"
    
    print(f"Ticket number: {suffix}, Response target: {target}")