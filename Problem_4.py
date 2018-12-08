a = list(filter(lambda x: x >= 0 , list(map(int, input().split()))))
i = min(a) 
while i in set(a): i += 1
print(i)    