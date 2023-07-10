#madlibs
adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
food = input("Food: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
noun1 = input("Noun: ")
room = input("Room: ")
bodypart = input("Bodypart: ")
pluralnoun = input("Plural Noun: ")

print("Welcome to Madlibs \n")
#using F string to store the variale and print it/
madlibs = f"It was a  {adj1} cold November day. I woke up to the  {adj2} smell of roasting of {food} downstairs.I  {verb1} downstairs to see if I could help with {verb2} the dinner. My mom said:See if {noun1} needs a fresh glass of orange juice. So I carried away the tray of glass full of orange juice to the {room} room. When I got there, I could not believe my {bodypart}. There  were {pluralnoun} on the table"
print(madlibs)
