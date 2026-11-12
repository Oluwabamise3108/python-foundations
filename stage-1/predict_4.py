code = "404"
print(code == 404)
print(int(code) == 404)
print(5 >= 5, 3 != 3)

hours = 30
if hours > 48:
    print("Critical")
elif hours > 24:
    print("Overdue")
elif hours > 12:
    print("Warning")
else:
    print("On track")
print("Done")

