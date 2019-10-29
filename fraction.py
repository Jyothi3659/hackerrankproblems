def add(arr):
    negative_count = 0
    positive_count = 0
    zero_count = 0
    for ele in arr:
        if ele > 0:
           positive_count += 1
        elif ele < 0:
           negative_count += 1
        else:
           zero_count += 1
    print(positive_count / len(arr))
    print(negative_count / len(arr))
    print(zero_count / len(arr))

add([5,-1,0,20,8,9])
