def solve(lst, n, lim, ans):
    if n == lim:
        ans.append(lst) 
    elif not n > lim:
        solve(list(lst) + [2], n+2, lim, ans)
        solve(list(lst) + [1], n+1, lim, ans) 

ans = [] 
solve([], 0, int(input()), ans)
print(ans)
