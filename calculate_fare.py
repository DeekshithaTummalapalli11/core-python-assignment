def calculate_fare(dist):
    base = 50
    per_km = 10
    return base + (dist * per_km)
trips = [5, 10, 3]
t = 0
for i in range(len(trips)):
    fare = calculate_fare(trips[i])
    t += fare
    print(f"Trip {i+1}: ${fare}")
print("Total Fare: $", t)
