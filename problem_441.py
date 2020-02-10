def read_input():
    x = int(input())
    lst = list(map(int, input().split()))
    return x, lst 

def solve(lst, x):
    return list(filter(lambda y: y<x, lst)) + list(filter(lambda y: y == x, lst)) + list(filter(lambda y: y>x, lst))


x, lst = read_input()
print(solve(lst, x))