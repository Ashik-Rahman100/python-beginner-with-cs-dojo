# a set is a type of data that stories a set of things .

# A set of unique things . Python set not include a duplicate element.

a = set()
# print(a)

# set add element
a.add(1)
a.add(2)
a.add(3)
# print(a)

# iterate set same a list 
# for i in a:
    # print(i)

# list convert a set
numbers = [1,2,3,4,1,2,5]

new_set = set()
for i in numbers:
    new_set.add(i)

# print(new_set)

# set convert to list

new_list = []
for i in new_set:
    new_list.append(i)

# print(new_list)


# added with out duplicate number in list
list2 = [2,3,4,4,2]

new_set2 = set()
for i in list2:
    new_set2.add(i)
# print(new_set2)
total = 0
for i in new_set2:
    total += i

print(total)

