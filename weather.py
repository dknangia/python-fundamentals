temperature = 32
forecast = "sunny"
if temperature > 85 or temperature < 32 and forecast == "sunny":
    print("It's too hot outside.")
else:
    print("The weather is nice outside.")
    
if not forecast == "sunny":
    print("It's not sunny outside.")
else:
    print("It's sunny outside.")