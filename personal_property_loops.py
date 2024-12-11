"""
Personal Property Tax Calculator for Vehicles in Charlottesville
Created by: Jarullah Bana
"""

import datetime

def calculate_tax():
    # Constants
    TAX_RATE = 0.044  # 4.40% annual tax rate
    RELIEF_PERCENT = 0.30  # 30% relief for eligible vehicles
    
    while True:
        # Input: Assessed value of the vehicle
        try:
            assessed_value = float(input("Enter the assessed value of the vehicle: $"))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Input: Eligibility for tax relief
        eligible_input = input("Is your vehicle eligible for tax relief? (Y for Yes, N for No): ").strip().upper()
        if eligible_input not in ["Y", "N"]:
            print("Invalid input. Please enter Y or N.")
            continue
        is_eligible = eligible_input == "Y"
        
        # Calculations
        annual_tax = assessed_value * TAX_RATE
        six_month_tax = annual_tax / 2
        relief_amount = six_month_tax * RELIEF_PERCENT if is_eligible else 0
        total_due = six_month_tax - relief_amount
        
        # Get current date and time
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Display results
        print("\nPERSONAL PROPERTY TAX BILL")
        print(f"Prepared by: Farmadeh Bana")
        print(f"Date/Time: {current_date}")
        print(f"Assessed Value:           ${assessed_value:,.2f}")
        print(f"Full Annual Tax Amount:   ${annual_tax:,.2f}")
        print(f"Relief Amount:            ${relief_amount:,.2f}")
        print(f"Total Due (6 months):     ${total_due:,.2f}")
        
        # Ask if user wants to calculate for another vehicle
        another = input("\nWould you like to calculate tax for another vehicle? (Y/N): ").strip().upper()
        if another != "Y":
            print("Thank you for using the Personal Property Tax calculator.")
            break

# Run the program
if __name__ == "__main__":
    calculate_tax()
