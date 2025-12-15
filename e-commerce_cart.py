def calculate_total(cart):
    if not cart:          
        return 0
    total = 0
    for price in cart.values():
        total += price
    if len(cart) > 5:    
        total *= 0.9
    return total

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total_price = calculate_total(cart_items)
print("Total Price:", int(total_price))


