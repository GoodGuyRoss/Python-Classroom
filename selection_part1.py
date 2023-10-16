age = (int(input("How old are you?: ")))

if age > 17 or age == 18:
    print("You are in Category A.")
elif age > 16:
    print ("You are in Category B.")
elif age < 16:
    print("You are in Category C.")
else:
    print("That isn't a number, please re enter: ")
    18