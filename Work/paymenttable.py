# paymenttable.py
#
# Exercise 1.10
principal = 500_000
rate = 0.05 
total_paid = 0.0
months = 0
payment = 2684.11

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    months += 1
    if extra_payment_start_month <= months <= extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment
    
    interest = principal * (rate / 12)

    if principal + interest <= current_payment:
        principal = 0
    else:
        principal = principal + interest - current_payment
    total_paid += current_payment


    print(months, total_paid, principal)
