def solve(lst):
    ans = 1 
    for i in lst:
        if i <= ans:
            ans += i
    return ans 


print(solve(list(map(int, input().split()))))
