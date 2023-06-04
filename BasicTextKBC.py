#Very Basic and Simple KBC
print("Welcome to KBC") 
print("\n Please Select Your Choice From Following.")
print("1.Easy")
print("2.Medium")
print("3. Exit ")
a = int(input("enter your choice:"))
if a == 1:
  print("here is easiest que:")
  print("what is capital of India")
  print("Delhi")
  print("Mumbai")
  print("None")
  a = int(input("Enter Your Choice:"))
  if a ==1:
    print("Correct Ans")
  else:
    print("Wrong")
elif a == 2:
  print("Medium level question")
  print("Who wrote the constitution")
  print("Jawaharlaal Nehru")
  print("Dr.Babasaheb Ambedkar")
  print("None")
  a = int(input("Enter Your Choice:"))
  if a ==1:
    print("Correct Ans")
  else:
    print("Wrong")
else:
  print("YOU ARE OUT")
  

