# [expression for item in list]


# b = []
# b.append(10)
# b.append(20)

# print(b) //[10,20]

# In-general way list multiplay
a = [1,3,5,7,9,11]

new_list = []
for item in a:
    new_list.append(item * 2)

# print(new_list)

# list comprehensions
# [expression for item in list]

multilay =  [x*2 for x in a]
# print(multilay)

# squre number in general
square = []

for i in range(1,7):
    square.append(i ** 2)

# print(square)

# list comprehensions
square2 = [x ** 2 for x in range(1,7)]
# print(square2)

square3 = []
for i in range (6, 0, -1):
    square3.append(i**2)
# print(square3)


# list comprensions

square4 = [x**2 for x in range(6,0,-1)]
print(square4)
