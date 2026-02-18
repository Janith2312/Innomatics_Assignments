emails = [
    "ravi@gmail.com",
    "anita@yahoo.com",
    "kiran@gmail.com",
    "suresh@gmail.com",
    "meena@yahoo.com"
]

domain_count = {}

for email in emails:
    domain = email.split("@")[1]
    domain_count[domain] = domain_count.get(domain, 0) + 1

total_emails = len(emails)

for domain, count in domain_count.items():
    percentage = (count / total_emails) * 100
    print(f"{domain}: {int(percentage)}%")
