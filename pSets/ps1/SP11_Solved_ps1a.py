#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:09:40 2020

MIT Intro to Python 6.000 SP11
Problem Set 1
@author: rkotelova
"""

#minMonthlyPayment = minMonth_payRate x outstanding_balance
#(Minimum monthly payment gets split into interest paid and principal paid) 
#interestPaid = monthlyRate x outstanding_balance
#principalPaid = minMonthlyPayment – interestPaid
#rem_Balance = outstanding_balance – principalPaid


from collections import Counter
month_counter = Counter()

outstanding_balance = float(input("Enter the outstanding balance on your credit card: "))
annual_interest_rate = float(input("Enter your annual interest rate, as a decimal: "))
minMonth_payRate = float(input("Enter your minimum monthly payment rate, as a decimal: "))

# outstanding_balance = 4800
# annual_interest_rate = 0.2
# minMonth_payRate = 0.02

monthlyRate = annual_interest_rate/12.0
month_counter = 0 
totalPaid = 0

while month_counter < 12: 
    month_counter = month_counter + 1
    print("Month: ", month_counter)
   
    minMonthlyPayment = round(((minMonth_payRate) * (outstanding_balance)),2)
    print("Minimum monthly payment: $",minMonthlyPayment)
   
    interestPaid = (monthlyRate) * (outstanding_balance)
    principalPaid = round(((minMonthlyPayment)-(interestPaid)),2)
    print("Principal paid: $",principalPaid)
   
    rem_Balance = round(((outstanding_balance)-(principalPaid)),2)
    print ("Remaining balance: $",rem_Balance)
    outstanding_balance = rem_Balance
    
    totalPaid = totalPaid + minMonthlyPayment
    
print("RESULTS")
print("Total amount paid: $", totalPaid)
print("Remaining balance: $", outstanding_balance)
    
    
