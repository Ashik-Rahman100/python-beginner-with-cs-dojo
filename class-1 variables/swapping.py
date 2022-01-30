# Python swapping program  way 1

string_1 = "I'm first string";
string_2 = "I'm second string";

string_2 = string_1;
string_1 = string_2;

# print("String-1,",string_1, 'string-2,',string_2);

# Using two temporay variable then swapping string
var_1 = 'This is my First variable';
var_2 = 'This is my Second variable';

temp_1 = var_1;
temp_2 = var_2;
print('Before ','var_1:', var_1, 'var_2:', var_2);

var_1 = temp_2;
var_2 = temp_1;

print('Before ','var_1:', var_1, 'var_2:', var_2);


# python program swapping way 3 using  one temporary variable  # best practice
var1 = 'hello';
var2 = 'world';

temp = var1;
var1 = var2;

# print(var1, var2)
var2 = temp;
# print(var1,var2)



