'''
This problem was asked by Facebook.
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''
import numpy as np 
arr = list(map(int, input().split()))

#simulate input stream
for i in arr:
    if np.random.randint(2) == 0:
        print(i) 

#Probability that an element gets picked is 50/50 