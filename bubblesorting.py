n = 3
a = [3,2,1]
def bubble_sorting(a):
    numSwaps = 0
    for i in range(n):
        for j in range(0,n-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numSwaps += 1
    return numSwaps
# print(bubble_sorting(a))
    # return "Array is sorted in {}".format(numSwaps), "swaps."
    # print("First Element: {}".format(a[0]))
    # print("Last Element: {}".format(a[n-1]))
