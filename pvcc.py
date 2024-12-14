# Name: Jarullah Bana
# Program Purpose: This program calculates the cost of tuition, fees, and the remaining balance after applying a scholarship.
# The output is sent to an .html file

import datetime

##############  define global variables ############
# Define tax rate and prices
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# Define global variables
inout = 1  # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

# Create output file
outfile = 'tuition_report.html'

##############  define program functions ################
def main():
    open_outfile()
    more_students = True

    while more_students:
        get_user_data()
        perform_calculations()
        create_output_file()

        ask_again = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if ask_again.upper() == 'N':
            more_students = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html><head><title>PVCC Tuition Report</title>\n')
    f.write('<style>td { text-align: right; }</style></head>\n')
    f.write('<body style="background-color: #505A5B; color: #FFFFFF; font-family: Arial;">\n')

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMMUNITY COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    act_fee = numcredits * RATE_ACTIVITY_FEE
    inst_fee = numcredits * RATE_INSTITUTION_FEE
    total = tuition + cap_fee + act_fee + inst_fee
    balance = total - scholarship_amt

def create_output_file():
    currency_format = "{:,.2f}"
    today = str(datetime.datetime.now())
    day_time = today[:16]

    f.write('<table border="3" style="background-color: #94B0DA; margin: auto;">\n')
    f.write('<tr><td colspan="3" style="text-align: center;"><h2>**** PIEDMONT VIRGINIA COMMUNITY COLLEGE ****</h2></td></tr>')
    f.write('<tr><td colspan="3" style="text-align: center;">*** Tuition and Fees Report ***</td></tr>')

    f.write(f'<tr><td>Tuition</td><td></td><td>{currency_format.format(tuition)}</td></tr>\n')
    f.write(f'<tr><td>Capital Fee</td><td></td><td>{currency_format.format(cap_fee)}</td></tr>\n')
    f.write(f'<tr><td>Institution Fee</td><td></td><td>{currency_format.format(inst_fee)}</td></tr>\n')
    f.write(f'<tr><td>Activity Fee</td><td></td><td>{currency_format.format(act_fee)}</td></tr>\n')
    f.write(f'<tr><td>Total</td><td></td><td>{currency_format.format(total)}</td></tr>\n')
    f.write(f'<tr><td>Remaining Balance</td><td></td><td>{currency_format.format(balance)}</td></tr>\n')

    f.write(f'<tr><td colspan="3" style="text-align: center;">Date/Time: {day_time}</td></tr>\n')
    f.write('</table><br />')

##########  call on main program to execute ############
main()
