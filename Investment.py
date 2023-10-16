inital_investment = float(input("intial investment: £"))
target_value = float(input("target value: £"))
interest_rate = float(input("interest rate: %")) /100

years = 0

while inital_investment < target_value:
    inital_investment *= interest_rate
    years += 1
    
print(f"it will take {years} years to get to £{target_value}")