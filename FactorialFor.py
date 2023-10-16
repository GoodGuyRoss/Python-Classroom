num = (int(input("Please input a number: ")))

factorial = 1
for i in range(1, num+1):
    factorial *= num 
    num -= 1
print("factorial: ", factorial)