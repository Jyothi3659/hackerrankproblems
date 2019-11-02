# You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is divisible by .
#
# For example,  and . Our three pairs meeting the criteria are  and .
#
# Function Description
#
# Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.
#
# divisibleSumPairs has the following parameter(s):
#
# n: the integer length of array
# ar: an array of integers
# k: the integer to divide the pair sum by
# Input Format
#
# The first line contains  space-separated integers,  and .
# The second line contains  space-separated integers describing the values of .
#
# Constraints
#
# Output Format
#
# Print the number of  pairs where  and  +  is evenly divisible by .
#
# Sample Input
#
# 6 3
# 1 3 2 6 1 2
# Sample Output
#
#  5
# Explanation
#
# Here are the 5 valid pairs when k = 3:
# (0,2)->ar[0]+ar[2]=1+2=3
# (0,5)->ar[0]+ar[5]=0+5=5
# (1,3)->ar[1]+ar[3]=3+6=9
# (2,4)->ar[2]+ar[4]=2+1=3
# (4,5)->ar[4]+ar[5]=1+2=3


def divisibleSumPairs(k, ar):
    count=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if(ar[i]+ar[j])%k==0:
                count+=1
    return count


k = 3
ar=[1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(k,ar))


