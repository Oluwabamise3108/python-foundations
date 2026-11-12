status_code = int(input("What is the HTTP status code? "))
if 200 <= status_code < 300:
    Status = "a Success"
elif 300 <= status_code < 400:
    Status = "a Redirect"
elif 400 <=  status_code < 500:
    Status = "a Client Error: check the request" 
elif 500 <= status_code < 600:
    Status = "a Server Error: escalate to engineering"
else:
    Status = "Not a valid HTTP status code"

print(f"HTTP status code {status_code} is {Status}")
