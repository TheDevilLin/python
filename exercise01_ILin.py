""" The Challenge
Aling Nena’s Sari-sari store wants a robot that will ask the customer
their total bill and payment amount and tell them their change
(for now, we can allow negative change).
"""

totalBill = float(input('What is your total bill? '))
paymentAmount = float(input('What is your payment amount? '))

finalAmount = totalBill - paymentAmount

print(f'Your change is {finalAmount}')