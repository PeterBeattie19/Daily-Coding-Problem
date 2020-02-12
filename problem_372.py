import math


def count_digits(n):
    return int(math.log(n ,10)) + 1 


input_ = int(input()) 
print(count_digits(input_))
