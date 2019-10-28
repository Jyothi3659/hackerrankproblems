def fraction(arr):
    postive_values = 0
    negative_values = 0
    zeros = 0
    for each in arr:
        if each > 0:
            postive_values += 1
        elif each < 0:
            negative_values += 1
        else:
            zeros += 1
    print(postive_values/len(arr))
    print(negative_values/len(arr))
    print(zeros/len(arr))
fraction([-1,-5,-4,0,-8,0])
