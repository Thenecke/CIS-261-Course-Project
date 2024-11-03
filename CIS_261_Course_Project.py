def calculate_payroll():
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_income_tax = 0
    total_net_pay = 0
     
    def get_date_range():

    while True:

        try:

           from_date = input("Enter From Date (mm/dd/yyyy): ")

           to_date = input("Enter To Date (mm/dd/yyyy): ")

           # Check if dates are in the correct format from_date = datetime.strptime(from_date,"%m/%d/%Y")

            to_date = datetime.strptime(to_date, "%m/%d/%Y") break

          except ValueError:

            print("Invalid date format. Please enter date in mm/dd/yyyy format.")

          return from_date.strftime("%m/%d/%Y"),

         to_date.strftime("%m/%d/%Y")
    while True:
        employee_name = input("Enter employee's name (or type 'end' to finish): ")
        if employee_name.lower() == 'end':
            break

        try:
            hours_worked = float(input(f"Enter total hours worked for {employee_name}: "))
            hourly_rate = float(input(f"Enter hourly rate for {employee_name}: "))
            tax_rate = float(input(f"Enter income tax rate for {employee_name} (as a percentage, e.g., 20 for 20%): ")) / 100
        except ValueError:
            print("Invalid input, please try again.")
            continue

        # Calculate pay
        gross_pay = hours_worked * hourly_rate
        income_tax = gross_pay * tax_rate
        net_pay = gross_pay - income_tax

        # Print employee payroll details
        print("\nEmployee Payroll Information:")
        print(f"Employee Name: {employee_name}")
        print(f"Total Hours Worked: {hours_worked}")
        print(f"Hourly Rate: ${hourly_rate:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f}")
        print(f"Income Tax Rate: {tax_rate * 100:.2f}%")
        print(f"Income Tax: ${income_tax:.2f}")
        print(f"Net Pay: ${net_pay:.2f}\n")

        # Update totals
        total_employees += 1
        total_hours += hours_worked
        total_gross_pay += gross_pay
        total_income_tax += income_tax
        total_net_pay += net_pay

    # Display totals for all employees
    print("\nFinal Totals:")
    print(f"Total Number of Employees: {total_employees}")
    print(f"Total Hours Worked: {total_hours:.2f}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Total Income Tax: ${total_income_tax:.2f}")
    print(f"Total Net Pay: ${total_net_pay:.2f}")

# Run the payroll calculation
calculate_payroll()
