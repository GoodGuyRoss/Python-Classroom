x = 1

for x in range (1,101):
    square = x**2
    if square > 2000:
        break
    print(x, "=", square)
    x += 1