# Given an array of integers, find and print the maximum number of integers you can select from the array such that the absolute difference between any two of the chosen integers is less than or equal to . For example, if your array is , you can create two subarrays meeting the criterion:  and . The maximum length subarray has  elements.
#
# Function Description
#
# Complete the pickingNumbers function in the editor below. It should return an integer that represents the length of the longest array that can be created.
#
# pickingNumbers has the following parameter(s):
#
# a: an array of integers
# Input Format
#
# The first line contains a single integer , the size of the array .
# The second line contains  space-separated integers .
#
# Constraints
#
# The answer will be .
# Output Format
#
# A single integer denoting the maximum number of integers you can choose from the array such that the absolute difference between any two of the chosen integers is .
#
# Sample Input 0
#
# 6
# 4 6 5 3 3 1
# Sample Output 0
#
# 3
# Explanation 0
#
# We choose the following multiset of integers from the array:{4,3,3} . Each pair in the multiset has an absolute difference <=1  (i.e.,|4-3|=1 and |3-3|=0), so we print the number of chosen integers,3, as our answer.
#
# Sample Input 1
#
# 6
# 1 2 2 3 1 2
# Sample Output 1
#
# 5
# Explanation 1
#
# We choose the following multiset of integers from the array:{1,2,2,1,2}.Each pair in the multiset has an absolute difference <=1(i.e.,|1-2|=1,|1-1|=0, and |2-2|=0), so we print the number of chosen integers,5, as our answer.
#

def pickingNumbers(a):
    maximum = 0
    diff = 1

    for k in a:
        n1 = a.count(k)
        n2 = a.count(k-diff)
        maximum = max(maximum, n1+n2)
    return maximum


a = ([3,3,3,4,1,5,10,5])
print(pickingNumbers(a))



