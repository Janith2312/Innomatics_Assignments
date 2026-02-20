Base_fare = "₹50"
per_km_rate = "₹12/km"
peak_hour_rate = "₹15/km"
distance_km = float(input("Enter the distance of the ride in kilometers: "))
is_peak_hour = input("Is it peak hour? (yes/no): ").strip().lower()
def fare_estimation(distance_km, is_peak_hour):
    if is_peak_hour == "yes":
        fare = 50 + (distance_km * 15)
    else:
        fare = 50 + (distance_km * 12)
    return fare
estimated_fare = fare_estimation(distance_km, is_peak_hour)
print(f"Estimated fare for the ride: ₹{estimated_fare:.2f}")