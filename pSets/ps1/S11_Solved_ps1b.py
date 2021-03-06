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

#outstanding_balance = 1200
#annual_interest_rate = 0.18

monthlyRate = annual_interest_rate/12.0
month_counter = 0 
totalPaid = 0
minMonthlyPayment = 10
outstanding_balance_res = outstanding_balance

def resetVar():
    global outstanding_balance, month_counter, totalPaid
    outstanding_balance = outstanding_balance_res
    month_counter = 0 
    totalPaid = 0
   
while totalPaid < outstanding_balance:   
    if minMonthlyPayment % 10 == 0 and ((outstanding_balance / minMonthlyPayment) < 12):
     
        while outstanding_balance > 0 and month_counter < 12:
            month_counter = month_counter + 1
            outstanding_balance = (outstanding_balance * (1 + monthlyRate)) - minMonthlyPayment
            totalPaid = totalPaid + minMonthlyPayment  
            
        if outstanding_balance > 0:
            minMonthlyPayment = minMonthlyPayment + 10
            resetVar()   
    else: 
        minMonthlyPayment = minMonthlyPayment + 10
  
balance = round(outstanding_balance, 2)
print("Monthly payment to pay off debt in 1 year: $", minMonthlyPayment) 
print("Number of months needed: ", month_counter)
print("Balance: $", balance)
       
