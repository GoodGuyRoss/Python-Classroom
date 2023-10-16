#Sam has been dumped by his girlfriend so he's gone into the local milk 
#bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
#milkshakes, 
#differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
#number corresponding 
#to the relevant flavour - this list is displayed every iteration. 
#If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
#If he orders but can't pay he's thrown out.


shakes = {'1': ['Chocolate', 3], 
          '2': ['Marshmallow', 3],
          '3': ['Smmores', 4]}
budget = int(input("What's your budget for tonight then ay?: "))
while True:
  print("\n The Menu:")
  
  for key, shake in shakes.items():
    name, price = shake
    print(f"{key}: {name} (£{price})")
    
    choice = input("\nWhat can I fix you?: ")
    
    if choice == 'Q':
        print("\nI wish you luck on your dangerous journery throughout love Sammie boy.")
        break
    
  if choice in shakes:
    name, price = shakes[choice]
    
    if price <= budget:
      print(f"\nHave a lovely {name} milkshake")
      budget -= price
      
    else:
      print("\nYou're out of dosh, buzz off!")
      break
    
  else:
    print("\nNot a milkshake I've ever heard of.")  
    
print("\nLater Alligator")
    
    
        
    