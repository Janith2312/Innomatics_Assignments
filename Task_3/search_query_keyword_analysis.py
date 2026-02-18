employees = {
    "Ravi": 92,
    "Anita": 88,
    "Kiran": 92,
    "Suresh": 85
}

top_score = max(employees.values())

top_performers = []
for name, score in employees.items():
    if score == top_score:
        top_performers.append(name)

print(f"Top Performers Eligible for Bonus: {', '.join(top_performers)} (Score: {top_score})")
