# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#total_cost = 1,000,000
#annual_salary = 100,000
#portion_saved = 0.1

      #  monthly contribution = annual_salary/12 * portion_saved 
      #  for each month that I save multiply that sum by r :
      #  count how many months it would take 
      #  to downpayment >current_savings

from collections import Counter
month_counter = Counter()


annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the total cost of your dream home: "))
semi_annual_raise = float(input("Enter the percent of your 6 month raise, as a decimal: ")) 

r = 0.04/12
portion_down_payment = total_cost * 0.25

monthly_savings = ((annual_salary/12) * portion_saved)

#print ("Monthly savings: ") 
#print (monthly)
current_savings = 0
#print (current_savings)
month_counter = 0


while current_savings < portion_down_payment:
    month_counter = month_counter + 1
 
    if month_counter % 6 == 0:
        annual_salary = (annual_salary) + (annual_salary * semi_annual_raise)
        monthly_savings = ((annual_salary/12) * portion_saved)
        current_savings = ((current_savings) + (current_savings * r)) + monthly_savings
   
    else:    
        current_savings = ((current_savings) + (current_savings * r)) + monthly_savings
        
    #print(current_savings)
    #print(c)
    # if current_savings == portion_down_payment:
    #     break
    print ("Current savings: ", current_savings)
    print ("Number of months: ", month_counter)
    
            
        
