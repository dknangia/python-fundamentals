age = int(input("How old are you?\n"))
decades = age // 10
years = age % 10
print("You are are", str(decades) + " decades old, and " + str(years) + " year", years>1 and "s" or "" + " old.")

