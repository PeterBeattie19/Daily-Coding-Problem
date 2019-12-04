def read_input():
    return list(map(int, input().split())) 


def get_longest_sequence(arr):
    arr.sort()
    global_arr, local_arr = [], [arr[0]] 

    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i]) == 1:
            local_arr.append(arr[i+1]) 
        else:
            global_arr = local_arr if len(global_arr) < len(local_arr) else global_arr
            local_arr = [arr[i+1]]
    return global_arr



lst = read_input() 
print(get_longest_sequence(lst))
