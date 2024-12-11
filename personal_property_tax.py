import datetime

# Program: Personal Property Tax Report
# Author: Jarullah Bana
# Description: This program calculates the personal property tax for vehicles in Charlottesville
# using data stored in lists and generates a report.

# Define tax rates
PPT_RATE = 0.042  # Personal Property Tax Rate (4.2% annually)
RELIEF_RATE = 0.33  # Tax Relief Rate (33%)

# Create list data
vehicles = ["2019 Volvo", "2018 Toyota", "2022 Kia", "2020 Ford", "2023 Honda", "2019 Lexus"]
vehicle_values = [13000, 10200, 17000, 21000, 28000, 16700]
pptr_eligible = [True, True, False, True, False, True]
owner_names = ["Brand Debra", "Smith Carter", "Johnson Bradley", "Garcia Jennifer", "Henderson Leticia", "White Leticia"]

# Define function to calculate personal property tax
def calculate_tax(vehicle_value, eligible):
    annual_tax = vehicle_value * PPT_RATE
    semi_annual_tax = annual_tax / 2
    if eligible:
        relief = semi_annual_tax * RELIEF_RATE
        return semi_annual_tax - relief
    else:
        return semi_annual_tax

def main():
    ppt_owed = []
    total_tax_due = 0

    # Perform calculations
    for i in range(len(vehicles)):
        tax_due = calculate_tax(vehicle_values[i], pptr_eligible[i])
        ppt_owed.append(tax_due)
        total_tax_due += tax_due

    # Generate report
    print("Charlottesville Personal Property Tax Report")
    print(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"{'Owner':<20}{'Vehicle':<20}{'Tax Due ($)':<10}")
    print("-" * 50)

    for i in range(len(vehicles)):
        print(f"{owner_names[i]:<20}{vehicles[i]:<20}{ppt_owed[i]:<10.2f}")

    print("-" * 50)
    print(f"{'Total Tax Due:':<40}{total_tax_due:.2f}")

if __name__ == "__main__":
    main()
