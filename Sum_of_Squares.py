x = eval(input("Enter the number of squares you want to sum: "))
sum = 0
for i in range(x):
    y = eval(input("Enter a number to be squared: "))
    y = y ** 2
    sum += y

print(sum)