# Request input from user 
x = eval(input("Enter the number of squares you want to sum: "))

# Initiate for loop
sum = 0
for i in range(x):
    y = eval(input("Enter a number to be squared: "))
    y = y ** 2     # square number
    sum += y       # add to sum

# Print result
print(sum)