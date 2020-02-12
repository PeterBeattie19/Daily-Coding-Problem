def solve(lst):
    for i in range(len(lst)):
        if lst[i] < len(lst) and lst[i] >= 0:
            if lst[lst[i]] == lst[i]:
                return i


print(solve(list(map(int, input().split()))))
