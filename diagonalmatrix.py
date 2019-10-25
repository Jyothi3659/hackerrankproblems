# Print the absolute difference between the sums of the matrix's two diagonals as a single integer.
#
# Sample Input
#
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output
#
# 15
# Explanation
#
# The primary diagonal is:
#
# 11
#    5
#      -12
# Sum across the primary diagonal: 11 + 5 - 12 = 4
#
# The secondary diagonal is:
#
#      4
#    5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15


def difference(arr):
    d1 = 0
    d2 = 0
    for i in range(0,n):
        for j in range(0,n):
            if (i==j):
                d1 += arr[i][j]
            if (i == n-j-1):
                d2 += arr[i][j]
    return d1-d2
n = 9
arr = [[6,6,7,-10,9,-3,8,9,-1],[9,7,-10,6,4,1,6,1,1],[-1,-2,4,-6,1,-4,-6,3,9],[-8,7,6,-1,-6,-6,6,-7,2],[-10,-4,9,1,-7,8,-5,3,-5],[-8,-3,-4,2,-3,7,-5,1,-5],
       [-2,-7,-4,8,3,-1,8,2,3],[-3,4,6,-7,-7,-8,-3,9,-6],[-2,0,5,4,4,4,-3,3,0]]
print(difference(arr))
import os
import math
# import os
import random
import re
import sys

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

        result = diagonalDifference(arr)

        fptr.write(str(result) + '\n')

        fptr.close()
        print(result)
