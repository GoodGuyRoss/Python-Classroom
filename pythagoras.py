def choice1(B, C):
    return B**2 + C**2

def choice2(A, C):
    return A**2 + C**2

def choice3(A,B):
    return A**2 + B**2


print("Pythagoras’ Calculator")
print("1. Find the length of A given B and C")
print("2. Find the length of B given A and C")
print("3. Find the length of C given A and B")

choice = (int(input("Enter choice(1, 2, 3): ")))


if choice == 1:
    B = (int(input("Please enter value B: ")))
    C = (int(input("Please enter value C: ")))
    print(B, "**", C, "=", choice1(B, C))
elif choice == 2:
    A = (int(input("Please enter value A: ")))
    C = (int(input("Please enter value C: ")))
    print(A, "**", C, "=", choice2(A, C))
elif choice == 3:
    A = (int(input("Please enter value A: ")))
    B = (int(input("Please enter value B: ")))
    print(A, "**", B, "=", choice3(A, B))
    
else:
    print("Not a valid choice. Retry: ")