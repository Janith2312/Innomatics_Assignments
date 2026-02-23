def transaction_check(amount):
    if amount <= 50000:
        status = "Approved"
    else:
        status = "Rejected"

    print("Transaction Amount:", amount)
    print("Transaction Status:", status)

transaction_check(60000)