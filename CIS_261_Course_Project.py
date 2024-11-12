# Function to input the from date and to date for hours worked
from datetime import datetime


def get_date_range():
    while True:
        try:
            from_date = input("Enter From Date (mm/dd/yyyy): ")
            to_date = input("Enter To Date (mm/dd/yyyy): ")
            # Check if dates are in the correct format
            from_date = datetime.strptime(from_date, "%m/%d/%Y")
            to_date = datetime.strptime(to_date, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter date in mm/dd/yyyy format.")
    return from_date.strftime("%m/%d/%Y"), to_date.strftime("%m/%d/%Y")

# Function to input employee data and calculate payroll details
def calculate_payroll():
    employees_data = []
    
    while True:
        employee_name = input("Enter employee's name (or type 'end' to finish): ")
        if employee_name.lower() == 'end':
            break

        # Call the date input function to get from and to dates
        from_date, to_date = get_date_range()

        try:
            hours_worked = float(input(f"Enter total hours worked for {employee_name}: "))
            hourly_rate = float(input(f"Enter hourly rate for {employee_name}: "))
            tax_rate = float(input(f"Enter income tax rate for {employee_name} (as a percentage, e.g., 20 for 20%): ")) / 100
        except ValueError:
            print("Invalid input, please try again.")
            continue
        
        # Store the employee's data in a list
        employees_data.append([from_date, to_date, employee_name, hours_worked, hourly_rate, tax_rate])

    return employees_data

# Function to calculate payroll details and display results
def calculate_employee_payroll(employees_data):
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_income_tax = 0
    total_net_pay = 0

    # Dictionary to hold totals
    totals = {
        'total_employees': 0,
        'total_hours': 0,
        'total_gross_pay': 0,
        'total_income_tax': 0,
        'total_net_pay': 0
    }

    print("\nEmployee Payroll Information:")

    for employee in employees_data:
        from_date, to_date, name, hours_worked, hourly_rate, tax_rate = employee

        # Calculate payroll details
        gross_pay = hours_worked * hourly_rate
        income_tax = gross_pay * tax_rate
        net_pay = gross_pay - income_tax

        # Display individual employee payroll details
        print(f"\nFrom Date: {from_date}")
        print(f"To Date: {to_date}")
        print(f"Employee Name: {name}")
        print(f"Total Hours Worked: {hours_worked}")
        print(f"Hourly Rate: ${hourly_rate:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Income Tax Rate: {tax_rate * 100:.2f}%")
        print(f"Income Tax: ${income_tax:.2f}")
        print(f"Net Pay: ${net_pay:.2f}")

        # Update totals
        totals['total_employees'] += 1
        totals['total_hours'] += hours_worked
        totals['total_gross_pay'] += gross_pay
        totals['total_income_tax'] += income_tax
        totals['total_net_pay'] += net_pay

    return totals

# Function to display total summary
def display_totals(totals):
    print("\n--- Totals Summary ---")
    print(f"Total Number of Employees: {totals['total_employees']}")
    print(f"Total Hours Worked: {totals['total_hours']:.2f}")
    print(f"Total Gross Pay: ${totals['total_gross_pay']:.2f}")
    print(f"Total Income Tax: ${totals['total_income_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")

# Main function to run the program
def main():
    employees_data = calculate_payroll()
    
    # If no employees were entered, notify the user
    if not employees_data:
        print("No employee data entered.")
    else:
        # Calculate and display employee payroll
        totals = calculate_employee_payroll(employees_data)
        
        # Display totals summary
        display_totals(totals)

# Run the payroll calculation
if __name__ == "__main__":
    main()
