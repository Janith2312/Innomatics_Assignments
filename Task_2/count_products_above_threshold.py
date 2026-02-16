prices = [450, 1200, 899, 1500, 300]
threshold = 1000
products_above_threshold = []
for price in prices:
    if price > threshold:
        products_above_threshold.append(price)
print("Products above 1000:", len(products_above_threshold))