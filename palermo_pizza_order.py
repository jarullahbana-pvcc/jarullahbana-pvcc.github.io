from datetime import datetime

# Prices and tax rate
PIZZA_PRICES = {'S': 9.99, 'M': 12.99, 'L': 17.99, 'X': 21.99}
DRINK_PRICE = 3.99
BREADSTICK_PRICE = 6.99
SALES_TAX_RATE = 0.055

# Get user input
print("Welcome to Palermo Pizza!")
print("Pizza Sizes: S (Small - $9.99), M (Medium - $12.99), L (Large - $17.99), X (Extra Large - $21.99)")
pizza_size = input("Enter pizza size (S, M, L, X): ").upper()
num_pizzas = int(input("Enter the number of pizzas: "))
num_drinks = int(input("Enter the number of drinks: "))
num_breadsticks = int(input("Enter the number of breadstick orders: "))

# Calculate costs
pizza_cost = num_pizzas * PIZZA_PRICES.get(pizza_size, 0)
drink_cost = num_drinks * DRINK_PRICE
breadstick_cost = num_breadsticks * BREADSTICK_PRICE
subtotal = pizza_cost + drink_cost + breadstick_cost
sales_tax = subtotal * SALES_TAX_RATE
total = subtotal + sales_tax

# Display the receipt
def display_results():
    print("\n--- Palermo Pizza Receipt ---")
    print(f"Date & Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Number of Pizzas Ordered: {num_pizzas}")
    print(f"Pizza Size: {pizza_size} - Cost: ${pizza_cost:.2f}")
    print(f"Drinks Cost: ${drink_cost:.2f}")
    print(f"Breadsticks Cost: ${breadstick_cost:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax (5.5%): ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("----------------------------")
    print("Thank you for ordering with Palermo Pizza!")

# Call function to display receipt
display_results()
