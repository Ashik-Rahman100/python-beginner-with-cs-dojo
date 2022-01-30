
# python problem solving 
frutes = ["apple","banana","orange"];

'''
# iterate a list
for item in frutes:
    print(item);
'''
'''
# range method
for i in range(len(frutes)):
    for j in range(i+1):
     print(frutes[i]);
'''

'''
# print (list(range(1,100)));
# problem-1: sum of just divide 3 and 5 their number.
total =0

for i in range(1,100):
    if ((i%3 == 0) or(i%5 == 0)):
        total += i
    # elif(i%5 == 0):
    #     total += i

print(total)
'''

# desending number of sum
numbers  = [7,5,4,4,3,1,-2,-3,-5,-7]

total = 0
j = len(numbers) - 1

while numbers[j] < 0:
    total += numbers[j];
    j -= 1

print(total);


