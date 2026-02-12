username = "admin"
password = "1234"
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if input_username == username and input_password == password:
    print("Login successful")
else:
    print("Login failed")