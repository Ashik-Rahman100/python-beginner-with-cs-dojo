# boolean operator
import re


def are_you_sad(is_rainy, has_umbrella):
    return is_rainy and not has_umbrella 

    # if is_rainy == True and has_umbrella == False:
    #     return True
    # else:
    #     return Falsem 

result =  are_you_sad(True,False)
print(result)

# c geter than d, Plus e 
def c_greter_than_d_plus_e(c,d,e):
    return c > (d+e)

result1 = c_greter_than_d_plus_e(5,3,2)
print(result1)

