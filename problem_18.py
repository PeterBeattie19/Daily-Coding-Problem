'''
This problem was asked by Google.
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray (not subset) of length k.
For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
•	10 = max(10, 5, 2)
•	7 = max(5, 2, 7)
•	8 = max(2, 7, 8)
•	8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''
#Inputs
k = int(input())
arr = list(map(int, input().split())) 

#Filter to get values greater than k
vals = set(filter(lambda x: x >= k, arr)) 

#Compute all subarrays 
res = [[arr[i-1], arr[i], arr[i+1]] if arr[i] in vals else None for i in range(1,len(arr)-1)] 
#Edge Cases
if arr[0] in vals: res.append(arr[0:3])
if arr[-1] in vals: res.append(arr[-3:]) 

res = list(filter(lambda x: x != None, res))
print("\n".join(list(map(str, res))))