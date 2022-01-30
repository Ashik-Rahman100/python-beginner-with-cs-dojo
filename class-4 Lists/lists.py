# # declare Lists
# from operator import indexOf

# a = [3,10,-10];
# print(a);
# # add a new number
# a.append(1);
# print(a);

# # add a new string
# a.append("hello");
# print(a);

# # add a new lists
# a.append([1,2,3,5]);
# print(a);

# # add a lists but don't show square braket
# a.extend([10,11,12]);
# print(a);

# # update list item
# a[1] = 20;
# print(a);

# # list item swapping
# temp = a[0];
# a[0] = a[8];
# a[8] = temp;
# print(a);

# print(len(a));

# simple way swapping list item
fruets  = ['apple','banana','orange'];
fruets[0], fruets[2] = fruets[2], fruets[0];

print(fruets);
