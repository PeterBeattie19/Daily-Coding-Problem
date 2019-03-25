arr = list(map(int, input().split()))


def sort_square(x):
    return sorted(map(lambda y: y**2, x))


print(sort_square(arr))
