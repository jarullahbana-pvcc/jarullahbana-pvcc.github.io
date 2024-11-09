


# branch.py
# Program created by Jarullah Bana

import datetime

# Constants for pricing and fees
ADULT_PRICE = 19.95
CHILD_PRICE = 11.95
SERVICE_FEE_RATE = 0.10
SALES_TAX_RATE = 0.062

# Function to display the menu
def display_receipt(adults, children):
    # Calculate the meal costs
    adult_cost = adults * ADULT_PRICE
    child_cost = children * CHILD_PRICE
    subtotal = adult_cost + child_cost
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + service_fee + sales_tax

    # Get the current date and time
    current_time = datetime.datetime.now()

    # Format and display the receipt
    print("\n" + "=" * 40)
    print("   Branch Barbeque Buffet")
    print(f"   {current_time.strftime('%A, %B %d, %Y')}")
    print(f"   {current_time.strftime('%I:%M %p')}")
    print("-" * 40)
    print(f"Adult Meals: {adults:>2} x ${ADULT_PRICE:>6.2f} = ${adult_cost:>7.2f}")
    print(f"Child Meals: {children:>2} x ${CHILD_PRICE:>6.2f} = ${child_cost:>7.2f}")
    print("-" * 40)
    print(f"Subtotal:                ${subtotal:>7.2f}")
    print(f"Service Fee (10%):       ${service_fee:>7.2f}")
    print(f"Sales Tax (6.2%):        ${sales_tax:>7.2f}")
    print("-" * 40)
    print(f"Total:                   ${total:>7.2f}")
    print("=" * 40)

# Main function to loop through the program
def main():
    while True:
        print("\nWelcome to Branch Barbeque Buffet!")
        try:
            adults = int(input("Enter the number of adults: "))
            children = int(input("Enter the number of children: "))
        except ValueError:
            print("Please enter a valid number for adults and children.")
            continue
       
        # Display the receipt
        display_receipt(adults, children)
       
        # Ask if the user wants to order again
        another_order = input("\nWould you like to place another order? (yes/no): ").strip().lower()
        if another_order != 'yes':
            print("\nThank you for coming to Branch Barbeque Buffet! Enjoy your meal.")
            break

# Run the main function
if __name__ == "__main__":
    main()
