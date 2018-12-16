def solve(h, c, n, k, costs):
    print(h+1,c+1) 
    if h == (n-1):
        return costs[h][c] 

    return costs[h][c] + min([solve(h+1, i, n, k, costs) for i in list(filter(lambda x: x!=c, list(range(k))))]) 


n, k = map(int, input().split()) 
costs = [list(map(int, input().split())) for _ in range(n)] 

print(solve(-1, -1, n, k, costs)) 