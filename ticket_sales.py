# Ticket Sales Program - Created by Jarullah Bana

# Define the program functions

def get_user_data():
    # Get the user's ticket purchase details
    global subtotal
    subtotal = float(input("Enter the subtotal for tickets: $"))

def perform_calculations():
    # Calculate the sales tax and total
    global sales_tax, total
    sales_tax = subtotal * 0.10  # 10% sales tax
    total = subtotal + sales_tax

def display_results():
    # Display the formatted results
    print(f"Subtotal: ${subtotal:,.2f}")
    print(f"Sales Tax: ${sales_tax:,.2f}")
    print(f"Total: ${total:,.2f}")

def main():
    more_tickets = True
    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno.lower() != 'y':
            more_tickets = False
    print("Thank you for your order. Enjoy your movie!")

# Run the program
main()
