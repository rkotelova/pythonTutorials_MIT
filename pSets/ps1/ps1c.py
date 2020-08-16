# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

      # Your semiannual raise is .07 (7%) 
      # Your investments have an annual return of 0.04 (4%) 
      # The down payment is 0.25 (25%) of the cost of the house 
      # The cost of the house that you are saving for is $1M.

from collections import Counter
month_counter = Counter()


# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the total cost of your dream home: "))
# semi_annual_raise = float(input("Enter the percent of your 6 month raise, as a decimal: ")) 


annual_salary = float(input("Enter your starting annual salary: "))
annual_salary_res = annual_salary
total_cost = 1000000
portion_down_payment = total_cost * 0.25

monthly_savings = portion_down_payment / 36

semi_annual_raise = 0.07
r = 0.04/12
current_savings = 0
month_counter = 0
months = 36
portion_saved  = (monthly_savings / (annual_salary/12))

iterations = 0
low = 0
high = 10000
mid = (high + low)/2



while abs(current_savings - portion_down_payment) >= 100:
 
    while month_counter < months:
        month_counter = month_counter + 1
     
        if month_counter % 6 == 0:
            annual_salary = (annual_salary) + (annual_salary * semi_annual_raise)
            monthly_savings = ((annual_salary/12) * portion_saved)
            current_savings = ((current_savings) + (current_savings * r)) + monthly_savings
       
        else:    
            current_savings = ((current_savings) + (current_savings * r)) + monthly_savings
    
    portion_saved = ((portion_saved) * 10000)  
    
    if current_savings < portion_down_payment:
        low = mid  
    else: 
        high = portion_saved
    mid = (high + low)/2
    iterations += 1 

    portion_saved  = mid/10000
    
    if abs(current_savings - portion_down_payment) >= 100:
        def resetVar():
            global month_counter, annual_salary, current_savings
            month_counter = 0
            annual_salary = annual_salary_res
            current_savings = 0
        resetVar()
        
    monthly_savings = (annual_salary/12) * (portion_saved) 
        
if portion_saved > 1.0:
    print ("It is not possible to pay the downpayment in three years")
else:   
    print ("Best savings rate:", portion_saved)  
    print ("Steps in bisection search:", iterations)






   # def binary_search(x, search_list):
   #     iterations = 1
   #     left = 0 # Determines the starting index of the list we have to search in
   #     right = len(search_list)-1 # Determines the last index of the list we have to search in
   #     mid = (right + left)//2 # In Python, // means floored division, 
   #     while search_list[mid] != x: # If this is not our search element
   #         # If the current middle element is less than x then move the left next to mid
   #         # Else we move right next to mid
   #         if  search_list[mid] < x:
   #             left = mid + 1
   #         else:
   #             right = mid - 1
   #         mid = (right + left)//2
   #         iterations += 1
   #     print 'iterations = ',str(iterations)
   #     return mid

   # print(binary_search(32, [4,8,9,10,24,32,45,56]))




        

    

    
            
        
