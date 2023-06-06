#Basic Tip Calculator
print("Welcome Basic Tip Calculator") 
bill = float(input("Please enter the total bill\n"))
people = int(input("Please enter the total no of people\n"))
tip = float(input("Please enter the tip you would like to give\n"))
total_pay = bill*(1 + tip/100)
each_pay = round(total_pay/people, 2)
print(f"Each person should pay: {each_pay}")