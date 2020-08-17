#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:09:40 2020

MIT Intro to Python 6.000 SP11
Problem Set 1
@author: rkotelova
"""


#Monthly interest rate = Annual interest rate / 12.0 
#Updated balance each month = Previous balance * (1 + Monthly interest rate) – Minimum monthly payment



from collections import Counter
month_counter = Counter()

outstanding_balance = float(input("Enter the outstanding balance on your credit card: $"))
annual_interest_rate = float(input("Enter your annual interest rate, as a decimal: "))

#outstanding_balance = 320000
#annual_interest_rate = 0.2

monthlyRate = annual_interest_rate/12.0
month_counter = 0 
totalPaid = 0
outstanding_balance_res = outstanding_balance

iteration = 0
low = outstanding_balance / 12.0 
high = (outstanding_balance * (1 + (monthlyRate)) ** 12.0) / 12.0
mid = (high + low) / 2

minMonthlyPayment = mid
balance = outstanding_balance

def resetVar():
    global outstanding_balance, month_counter, totalPaid
    outstanding_balance = outstanding_balance_res
    month_counter = 0 
    totalPaid = 0

    
while abs(balance) > 0.1:        
 
    resetVar()    
  
    while outstanding_balance > 0 and month_counter < 12:
        month_counter = month_counter + 1
        outstanding_balance = (outstanding_balance * (1 + monthlyRate)) - minMonthlyPayment
        totalPaid = totalPaid + minMonthlyPayment 

    balance = round(outstanding_balance, 2) 
    
    if outstanding_balance > 0.1 :
        low = mid
         
    else:
        high = mid
    mid = (high + low) / 2
    minMonthlyPayment = mid
    iteration += 1
      
    
    
print("Monthly payment to pay off debt in 1 year: $", round(minMonthlyPayment,2)) 
print("Number of months needed: ", (month_counter))
print("Balance: $",balance)
print("Iterations: ",iteration)
          
 
