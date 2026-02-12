messages = ["Hi", "Welcome to the platform", "OK"]
for message in messages:
    length = len(message)

    if length > 10:
        flag = 1
    else:
        flag = 0

    print(f"Message: '{message}' , Length: {length} , Flag: {flag}")
