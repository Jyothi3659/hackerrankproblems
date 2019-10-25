def add(arr):
    negative_count = 0.0
    positive_count = 0.0
    zero_count = 0.0
    for next in arr:
        if next > 0:
          positive_count += 1
        elif next < 0:
          negative_count += 1
        else:
          zero_count += 1
    return arr


n = [-4, 2, -1, 30, 50]
print(add(n))
