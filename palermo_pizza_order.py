# Name: Jarullah Bana
# Program Purpose: This program calculates the cost of a meal at Palermo Pizza

import datetime

# Define global variables
PRICE_SMALL = 9.99
PRICE_MED = 12.99
PRICE_LARGE = 17.99
PRICE_XLARGE = 21.99
PRICE_DRINK = 1.99
PRICE_BREADSTICK = 4.99
TAX_RATE = 0.07  # 7% sales tax

# Define global variables to hold the data
num_pizzas = 0
num_drinks = 0
num_breadsticks = 0
cost_pizzas = 0
cost_drinks = 0
cost_breadsticks = 0
subtotal = 0
sales_tax = 0
total = 0

# Main function
def main():
    global more
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno.upper() == "N":
            more = False
            print("Thank you for your order. Enjoy your pizza!")

# Function to get user data
def get_user_data():
    global num_pizzas, num_drinks, num_breadsticks, pizza_size

    print('****** Palermo Pizza Menu ******')
    print(f'S Small Pizza \t $ {PRICE_SMALL:.2f}')
    print(f'M Medium Pizza \t $ {PRICE_MED:.2f}')
    print(f'L Large Pizza \t $ {PRICE_LARGE:.2f}')
    print(f'X Extra Large Pizza $ {PRICE_XLARGE:.2f}')
    print(f'D Drinks \t $ {PRICE_DRINK:.2f}')
    print(f'B Breadsticks \t $ {PRICE_BREADSTICK:.2f}')

    pizza_size = input("\nWhat size pizza would you like to order? (S, M, L, X): ").upper()
    while pizza_size not in ["S", "M", "L", "X"]:
        print("Invalid choice. Please enter S, M, L, or X.")
        pizza_size = input("What size pizza would you like to order? (S, M, L, X): ").upper()

    num_pizzas = int(input("Number of pizzas: "))
    num_drinks = int(input("Number of drinks: "))
    num_breadsticks = int(input("Number of breadstick orders: "))

# Function to perform calculations
def perform_calculations():
    global cost_pizzas, cost_drinks, cost_breadsticks, subtotal, sales_tax, total

    # Calculate pizza cost
    if pizza_size == "S":
        cost_pizzas = num_pizzas * PRICE_SMALL
    elif pizza_size == "M":
        cost_pizzas = num_pizzas * PRICE_MED
    elif pizza_size == "L":
        cost_pizzas = num_pizzas * PRICE_LARGE
    elif pizza_size == "X":
        cost_pizzas = num_pizzas * PRICE_XLARGE

    # Calculate drinks and breadsticks cost
    cost_drinks = num_drinks * PRICE_DRINK
    cost_breadsticks = num_breadsticks * PRICE_BREADSTICK

    # Calculate totals
    subtotal = cost_pizzas + cost_drinks + cost_breadsticks
    sales_tax = subtotal * TAX_RATE
    total = subtotal + sales_tax

# Function to display results
def display_results():
    global subtotal, sales_tax, total
    currency = "8,.2f"
    line = "-" * 30
    full_date = str(datetime.datetime.now())
    short_date = full_date[:16]

    print("\n" + line)
    print(f'****** Palermo Pizza ******')
    print(short_date)
    print(line)
    print(f'Number of pizzas ordered: {num_pizzas}')
    print(f'Cost of pizzas: \t $ {cost_pizzas:.2f}')
    print(f'Number of drinks ordered: {num_drinks}')
    print(f'Cost of drinks: \t $ {cost_drinks:.2f}')
    print(f'Number of breadsticks ordered: {num_breadsticks}')
    print(f'Cost of breadsticks: $ {cost_breadsticks:.2f}')
    print(line)
    print(f'Subtotal: \t \t $ {subtotal:.2f}')
    print(f'Sales Tax (7%): \t $ {sales_tax:.2f}')
    print(f'Total: \t \t $ {total:.2f}')
    print(line)

# Call the main function
main()
