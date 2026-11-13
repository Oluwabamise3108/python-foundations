# Ask for a username
username = input("Enter a username: ")
cleaned_username = username.strip().lower()

# 1. Is the username empty after cleaning
if not cleaned_username:
    print("Username cannot be empty. Please provide a valid username.")

# 2. Is there any space inside the username
elif " " in cleaned_username:
    print("Username cannot contain spaces. Please provide a valid username.")

# 3. Is the username between 3 and 15 characters long
elif not (3 <= len(cleaned_username) <= 15):
    print("Username must be between 3 and 15 characters long. Please provide a valid username.")

# 4. Does the username start with a digit?
elif cleaned_username[0].isdigit():
    print("Username cannot start with a digit. Please provide a valid username.")

else:
    print(f"Welcome '{cleaned_username}'! Your username is valid.")