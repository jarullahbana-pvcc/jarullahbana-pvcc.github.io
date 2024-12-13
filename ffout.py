# Name: Jarullah Bana
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ###########
emp = [
    "Smith, James",
    "Johnson, Patricia",
    "Williams, John",
    "Brown, Michael",
    "Jones, Elizabeth",
    "Garcia, Brian",
    "Miller, Deborah",
    "Davis, Timothy",
    "Rodriguez, Ronald",
    "Martinez, Karen",
    "Hernandez, Lisa",
    "Lopez, Nancy",
    "Gonzales, Betty",
    "Wilson, Sandra",
    "Anderson, Margie",
    "Thomas, Daniel",
    "Perez, Kevin",
    "Taylor, Steven",
    "Moore, Andrew",
    "Jackson, Donna",
    "Martin, Yolanda",
    "Lee, Carolina",
    "Thompson, Brian",
    "White, Deborah"
]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S", "J", "M", "C", "C", "S", "M", "J", "C", "S", "M", "C", "S"]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38, 28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

######## NEW LISTS for calculated amounts #####
gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0

##### TUPLES of constants #####
PAY_RATE = (16.50, 15.75, 15.75, 19.50)
DED_RATE = (.12, .03, .062, .0145, .04)  # federal, state, Social Security, Medicare, 401k

###### define program functions ######
def main():
    perform_calculations()
    display_results()
    create_output_file()

def perform_calculations():
    global total_gross, total_net

    for i in range(num_emps):
        # Calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:  # "M"
            pay = hours[i] * PAY_RATE[3]

        # Calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        ss = pay * DED_RATE[2]
        medicare_amt = pay * DED_RATE[3]
        retirement = pay * DED_RATE[4]
        
        # Calculate net pay
        net = pay - (fed + state + ss + medicare_amt + retirement)

        # Add to totals
        total_gross += pay
        total_net += net

        # Append amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(ss)
        medicare.append(medicare_amt)
        ret401k.append(retirement)
        net_pay.append(net)

def display_results():
    currency = '${:,.2f}'
    line = '-' * 80
    tab = "\t"

    print(line)
    print('**** FRESH FOODS MARKET ****')
    print('WEEKLY PAYROLL REPORT')
    print(tab + str(datetime.datetime.now()))
    print(line)

    titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
    print(titles1 + titles2)

    # Print out employee data
    for i in range(num_emps):
        data = (
            emp[i] + tab + job[i] + tab +
            currency.format(gross_pay[i]) + tab +
            currency.format(fed_tax[i]) + tab +
            currency.format(state_tax[i]) + tab +
            currency.format(soc_sec[i]) + tab +
            currency.format(medicare[i]) + tab +
            currency.format(net_pay[i])
        )
        print(data)

    print(line)
    print("***** TOTAL GROSS: " + currency.format(total_gross))
    print("***** TOTAL NET: " + currency.format(total_net))
    print(line)

def create_output_file():
    currency = '${:,.2f}'
    line = '-' * 80
    tab = "\t"

    out_file = "payroll.txt"
    with open(out_file, "w") as f:
        f.write(line + "\n")
        f.write('**** FRESH FOODS MARKET ****\n')
        f.write('WEEKLY PAYROLL REPORT\n')
        f.write(line + "\n")
        f.write(tab + str(datetime.datetime.now()) + "\n")
        f.write(line + "\n")

        titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
        titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
        f.write(titles1 + titles2 + "\n")

        for i in range(num_emps):
            data = (
                emp[i] + tab + job[i] + tab +
                currency.format(gross_pay[i]) + tab +
                currency.format(fed_tax[i]) + tab +
                currency.format(state_tax[i]) + tab +
                currency.format(soc_sec[i]) + tab +
                currency.format(medicare[i]) + tab +
                currency.format(net_pay[i]) + "\n"
            )
            f.write(data)

        f.write(line + "\n")
        f.write("***** TOTAL GROSS: " + currency.format(total_gross) + "\n")
        f.write("***** TOTAL NET: " + currency.format(total_net) + "\n")
        f.write(line + "\n")

    print("Open " + out_file + " to view your report")

########## call on main program to execute ##########
main()
