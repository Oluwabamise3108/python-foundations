status_code = int(input("What is the HTTP status code? "))
if 200 <= status_code < 300:
    status = "a Success"
elif 300 <= status_code < 400:
    status = "a Redirect"
elif 400 <= status_code < 500:
    status = "a Client Error: check the request" 
elif 500 <= status_code < 600:
    status = "a Server Error: escalate to engineering"
else:
    status = "Not a valid HTTP status code"

print(f"HTTP status code {status_code} is {status}")
