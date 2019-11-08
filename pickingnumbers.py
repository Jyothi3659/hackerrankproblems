from collections import defaultdict


def pickingNumbers(a):
    d = defaultdict(int)
    r_val = 0
    for val in a:
        d[val] += 1
        r_val = max(r_val, d[val] + d[val + 1], d[val] + d[val - 1])

    return r_val


a = ([3,3,3,4,1,5,10,5])
print(pickingNumbers(a))

