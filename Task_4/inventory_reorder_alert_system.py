inventory = {
    "item1": {"name": "Laptop", "quantity": 25},
    "item2": {"name": "Smartphone", "quantity": 10},
    "item3": {"name": "Headphones", "quantity": 20},
}   
reorder_threshold = 15
for item_id, item_info in inventory.items():
    if item_info["quantity"] < reorder_threshold:
        print(f"Reorder alert: {item_info['name']} (ID: {item_id}) has only {item_info['quantity']} units left.")
