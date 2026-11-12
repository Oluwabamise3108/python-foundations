ticket = "TCK-00123"
print(len(ticket))
print(ticket[0], ticket[3])
print(ticket[0:3])
print(ticket[4:])

priority = " HIGH "
priority.strip()
print(priority == "high")
cleaned = priority.strip().lower()
print(cleaned == "high")
print("time" in "Gateway timeout")