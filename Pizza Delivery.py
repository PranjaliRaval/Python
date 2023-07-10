#Basic Pizza Delivery
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

#here we are using the if elif else loop for size of pizza and then nesting if inside it for pepperoni. and creating separate if loop for extra cheese as it stays the same for any pizza
bill = 0 #initialsing bill with 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill +=20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill +=25
    if add_pepperoni == "Y":
        bill +=3
if extra_cheese == "Y":
    bill +=1
print(f"your final bill is: $ {bill}")
