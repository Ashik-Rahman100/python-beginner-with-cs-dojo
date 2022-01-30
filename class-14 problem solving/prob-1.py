#  prob-1: sleep in 
from unittest import result


def sleep_in(weekday,vacation):
    # if weekday == False or vacation == True:
    if not weekday  or vacation:
        return True
    else:
        return False

result1 =  sleep_in(False,False)
# print(result1)

# prob-2: repition string times
def string_times(str, n):
    return str * n

result2 = string_times("hello", 4)
# print(result2)

#problem-3 : print name

def hello_name(name):
    return f"Hello {name}!"

result3 = hello_name("Ashik")
# print(result3)

# problem-4: 1st element or last element = 6

def first_last(nums):
    if nums[0] == 6 or nums[-1]:
        return True
    else:
        return False

result4 = first_last([1,2,3,6])
# print(result4)


# problem-5: duble charecter print

def double_char(str):
    to_return = ''
    for c in str:
        to_return += c*2
    return to_return

result5 = double_char("ABC")
# print(result5)

# problem -6 : return number of even in the given array
def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += i
    return count

result6 = count_evens([2,1,2,3,4])
print(result6)
