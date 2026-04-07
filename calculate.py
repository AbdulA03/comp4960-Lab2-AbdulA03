BURGER_PRICE = 3.50
TAX_RATE = 0.08

burgers = int(input("Enter number of burgers: "))

subtotal = burgers * BURGER_PRICE
tax = subtotal * TAX_RATE
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
