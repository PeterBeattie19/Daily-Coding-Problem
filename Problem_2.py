from functools import reduce
arr = list(map(int, input().split()))
product = reduce(lambda x,y: x*y, arr) 
print(list(map(lambda x: product/x, arr))) 