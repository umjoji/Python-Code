sum = 0
y = 0
while y >= 0:
    y = eval(input("Enter a number: "))
    if y < 0:
        break
    else:
        sum += y

print(sum)