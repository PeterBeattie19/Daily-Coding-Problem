def solve(cust_drinks, cnt=0):
    if len(cust_drinks) == 0:
        return cnt 

    smll = min(cust_drinks) 
    best_drink = None
    cut_amount = 0 
    for drink in smll:
        current_cut = sum([drink in perf for perf in cust_drinks])
        if current_cut > cut_amount:
            cut_amount = current_cut
            best_drink = drink 
    
    return solve(list(filter(lambda x: best_drink not in x, cust_drinks)), cnt + 1) 


preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}

print(solve(list(map(set, preferences.values())))) 
