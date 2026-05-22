# Get details of the loan
money_owned = float(input("How much money do you owe, in dollars?\n"))
apr = float(input("How much is the annual rate of intrest?\n"))
payment = float(input("How much you pay for each month in dollars?\n"))
months = int(input("How many months do you want to see the results for?\n"))

# Calculate the monthly rate.
 
monthly_rate = apr/100/12
for i in range(months):
    intrest_paid = money_owned * monthly_rate
    money_owned = money_owned + intrest_paid
  
    
    if money_owned - payment < 0:
        print("The last payment is", money_owned)
        print("You paid off the loan in", i + 1, 'months')
        break
    money_owned = money_owned - payment
    print('Paid', payment, 'of which', intrest_paid , 'was intrest')
    print('Now I owe', money_owned)
    


