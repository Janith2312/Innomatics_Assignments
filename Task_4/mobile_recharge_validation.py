valid_plans = [199, 299, 399, 599]
user_plan = int(input("Enter the recharge plan amount: "))
while user_plan>50:
    if user_plan in valid_plans:
        print("Recharge successful!")
        break
    else:
        print("Invalid recharge plan. Please enter a valid amount.")
        user_plan = int(input("Enter the recharge plan amount: "))