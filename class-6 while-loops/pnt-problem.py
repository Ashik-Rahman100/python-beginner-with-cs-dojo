# problem 1: check even numbers and odd numbers

list1 = [1,2,3,4,5,6];
# list1 = [31,33,35]
sum1 = 0;
sum2 = 0;

for element in list1:
    if(element % 2 == 0):
        sum1 += element;
    else:
        sum2 += element;

print(sum1, sum2);

# Problem-2: length of numbers using function

def check_length(n):
    length = (len(n))
    return length;

user_input = input("Enter your input : ")  # input :123456, 
                                                    #  999
                                                    #  0
numbers_length = check_length(user_input);
print(numbers_length);

# problem-3 : find a dictionary maximum number

students =  {'st-01': 78, 'st-02': 56, 'st-03': 79, 'st-04': 77}
 # other input : {'s_01': 10, 's_04': 9}; output : s_01: 10


# max key
max_key = max(students, key = lambda x: students[x]);

# max Values
key_values = students.values();
max_value = max(key_values)
print(max_key, max_value);

#  problem-4: Take two name inputs, then print gmail address with a dot between the first name and last name, all lower case letters.

first_name = 'John';
second_name = 'Snow';

print(first_name+'.'+second_name+'@gmail.com');

# problem-5: Input two words, show the letters which are common in both words. If no match, then print "No Match"

first_word = input("Enter your first input: ");  #"dhaka"
second_word = input("Enter your second input: ")  #"khulna";

for i in first_word:
    for j in second_word:
        if(i == j):
            common_word = set(first_word)&set(second_word);
            print(common_word);
        else:
            print("No Match");

# problem 5 some problem .