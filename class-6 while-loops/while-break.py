
# # # using for loop
# total = 0;

# for i in range(1, 5):
#     total += i;
# print(total);

# # using while loop
# total1 = 0;
# i = 1;

# while i < 5:
#     total1 += i;
#     i += 1; 
# print(total1);


# numbers = [1,2,3,4,5,6];

# for i in numbers:
#     print (i)


# positive number added






# given_list = [5,4,3,5,8,6];

# total = 0;
# i = 0;

# while i < len(given_list) and given_list[i] > 0:
#     print(given_list[i])
#     total += given_list[i];
#     i += 1;
# print(total)


# break statement using in for loop 

given_list = [1,2,6,8,10,-2,-5,-3];
total = 0;

for element in given_list:
    if (element <= 0):
        break;
    total += element;
print(total)
    
# break statement using in while loop

total2 = 0;
i = 0;

while True:
    total2 += given_list[i];
    i += 1;

    if(given_list[i] <= 0):
        break;
print(total2);


