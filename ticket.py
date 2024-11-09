import datetime

# Program Name: Movie Tickets
# Author: Jarullah Bana
# Purpose: This program calculates the cost of movie tickets, including sales tax.
# Price for one ticket: $10.99
# Sales tax rate: 5.5%

# Define constants
SALES_TAX_RATE = 0.055  # 5.5% sales tax
PRICE_PER_TICKET = 10.99  # Price per ticket

# Global variables
num_tickets = 0
subtotal = 0.0
sales_tax = 0.0
total = 0.0

# Function to get the number of tickets from the user
def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

# Function to perform calculations
def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PRICE_PER_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

# Function to display the results
def display_results():
    print("\n*************************")
    print("CINEMA HOUSE MOVIES")
    print("Your neighborhood movie house")
    print(f"Tickets:       ${format(subtotal, '8,.2f')}")
    print(f"Sales Tax:     ${format(sales_tax, '8,.2f')}")
    print(f"Total:         ${format(total, '8,.2f')}")
    print("Date of Purchase:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("*************************\n")

# Main function to run the program and loop if the user wants to make another order
def main():
    more_tickets = True
    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()
       
        # Ask if the user wants to order more tickets
        yesno = input("\nWould you like to order again (Y or N)? ").lower()
        if yesno == "n":
            more_tickets = False
   
    print("Thank you for your order. Enjoy your movie!")

# Run the program
if __name__ == "__main__":
    main()
