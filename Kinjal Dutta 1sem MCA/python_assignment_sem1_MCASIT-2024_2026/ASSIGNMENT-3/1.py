overtime_rate = 12.0
regular_hours = 40

for i in range(1, 11):
    hours_worker = int(input("enter hours worked by employee{i}"))

    if hours_worker > regular_hours:
        overtime_hours  = hours_worker - regular_hours
        overtime_pay = overtime_hours  * overtime_rate
    else:
        overtime_pay = 0

    print(f"overtime pay for employee {i} is Rs.{overtime_pay}")