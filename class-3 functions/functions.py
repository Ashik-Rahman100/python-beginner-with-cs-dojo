# # What are functions?
# # Creating Bmi calculator

# # A function is collections of codes. or A function is collection of Instructions .
# # a function is a block of code that only runs when it is called .  Python functions return a value using a return statement.

# # declare a function
# # def function_name():
# #     print("Hello world");
# # print("end");


# # a mapping 
# # input or arguments or parameter

# # def functions (x):
# #     return x*2;

# # mult =  functions(5);
# # print(mult)

# # BMI calculator 
# from unicodedata import name


# def bmi_calculator(name,height_m,weigth_kg):
#     bmi = (weigth_kg / (height_m**2));
#     print("BMI :");
#     print("{:.2f}".format(bmi));

#     if(bmi<25):
#         return(name, "Your healthy is good");
#     else:
#         return(name, "Now you go to Gym . And exersize daily");

# name_1 = "Ashik Rahman";
# height_1 = 1.74;
# weight_1 = 54;
# result_1 = bmi_calculator(name_1,height_1,weight_1);
# print(result_1);

# name_2 = "sunny";
# height_2 = 2;
# weight_2 = 80;
# result_2 = bmi_calculator(name_2,height_2,weight_2);
# print(result_2);

# name_3 = "Junaed";
# height_3 = 1.5;
# weight_3 = 53;
# result_3 = bmi_calculator(name_3,height_3,weight_3);
# print(result_3);







 
# miles to kilomiters
def miles_to_kilomiter (miles):
    kilomiter = 1.6 * miles;
    return kilomiter;

result = miles_to_kilomiter(100);
print(result);

# meter to kilometer
def meter_to_kilometer(meter):
    kilometer = meter/1000;
    return kilometer;

kilometer_result = meter_to_kilometer(500);
print(kilometer_result)

