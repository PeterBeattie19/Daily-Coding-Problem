def solve(s, unique_chars):
    s = list(s)
    if not unique_chars.issubset(set(s)):
        return None
    front, back = 0, len(s)
    while True:
        if unique_chars.issubset(set(s[front+1:])):
            front += 1
        else:
            break
    
    while True:
        if unique_chars.issubset(set(s[front:back-1])):
            back -= 1 
        else:
            break 

    return s[front:back] if front < back else None
    

print("".join(solve(input(), set(['a', 'e', 'i'])) ))
