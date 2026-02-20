def check_password_strength(password):
    numbers = "0123456789"
    special_chars = "@#$%&*"

    has_number = False
    has_special = False

    # Check each character in password
    for ch in password:
        if ch in numbers:
            has_number = True
        if ch in special_chars:
            has_special = True

    # Validation rules
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    elif not has_number:
        return "Password must contain at least one number."
    elif not has_special:
        return "Password must contain at least one special character."
    else:
        return "Strong"


# Keep asking until password is strong
while True:
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)

    if result == "Strong":
        print("Strong Password ")
        break
    else:
        print("Weak Password :", result)
        print("Please try again.\n")