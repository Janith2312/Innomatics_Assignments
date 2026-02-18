sales = [1200, 1500, 900, 2200, 1400, 3000]
average_sales = sum(sales) / len(sales)
spike = average_sales * 1.3
for i, sale in enumerate(sales):
    if sale > spike:
        print(f"Day {i+1}: {sale}")