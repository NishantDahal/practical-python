# extrapayments.py
#
# Exercise 1.8
principal = 500_000
rate = 0.05
total_paid = 0.0
months = 0

while principal > 0:
    if months < 12:
        payment = 3684.11
    else:
        payment = 2684.11
    
    principal = principal * (1 + rate/12) - payment
    total_paid += payment
    months += 1

print(f'Total payment of {total_paid} over {months} months')
