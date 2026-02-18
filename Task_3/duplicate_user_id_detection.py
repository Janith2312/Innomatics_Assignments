user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]
counter = {}
for user_id in user_ids:
    if user_id in counter:
        counter[user_id] += 1
    else:
        counter[user_id] = 1
for user_id, count in counter.items():
    if count > 1:
        print(f"{user_id} → {count} times")