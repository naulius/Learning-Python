stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]
for item in stock_prices:
    print(item)

# You can also unpack tuples.
for ticker, price in stock_prices:
    print(ticker)

for ticker, price in stock_prices:
    print(price+(0.1*price))

work_hours = [("Abby", 100), ("Billy", 400), ("Cassie", 800)]
def employee_check(work_hours):
    """
    This function finds the employee with the most hours of work.

    :param work_hours: list of Tuples where you find the name of the employee and the hours that they work.
    :return: A Tuple with the name of the employee with max hours of work.
    """
    current_max = 0
    employee_of_month = None

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return(employee_of_month, current_max)
print(employee_check(work_hours))

