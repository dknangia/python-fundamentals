expenses = [10.5, 20.0, 5.75, 15.25, 8.0]

total_1 = 0

for x in expenses: # Iterate through each expense in the list, notice the ":"   
    total_1 = total_1 + x
    
print("Total expenses: $", total_1, sep="") # Print the total expenses, notice the "sep" parameter to add a space between the text and the sum


#shortcut to sum 
total = sum(expenses) # This will give the same result as the loop above, but it's more concise and efficient.
print("Total expenses: $", total, sep="") # Print the total expenses using the sum function.