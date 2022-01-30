'''
    # if statement
a = 13;
b = 2;

if(a < b):
    print('A is Less Then B');
    print('A is Defenetly less then b.');
print('Not sure if a is less then b.')
'''



'''
    # if-else statement
c = 4;
d = 5;

if(c < d):
    print("C Less Then D");
    print("C defenetly less then d");
else:
    print("c getter then d.");
    print("I don't think c is less then d.");

print("The program end.")

'''

'''
    
# if-elif-else
e = 28;
f = 7;

if(e < f):
    print("E is less then F");
elif(e == f):
    print("E Equal F");
elif(e > f+20 ):
    print("E getter than f by more than 10.")
else:
    print("E is getter then F");
'''

'''
    
# nested is if else 
g = 15;
h = 15;

if(g<h):
    print("H is getter than G");
else:
    if(g == h):
        print("G equal H");
    else:
        print("g is getter than H.");

'''

# simple BMI Calculator
name = 'Ashik Rahman';
height_m = 1.73;
weight_kg = 54;

bmi = (weight_kg / (height_m ** 2));
print("BMI : ")
print("{:.2f}".format(bmi))

if( bmi < 25):
    print(name," Your Healthy is  Perfect");
else:
    print(name," Please Now You to gym ...");

print('Program is Ended.');
