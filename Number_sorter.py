# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(n):
	ele = int(input("Enter list elements: "))

	lst.append(ele) # adding the element
list = sorted(lst)
print(list)

