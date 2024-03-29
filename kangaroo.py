# You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).
#
# The first kangaroo starts at location  and moves at a rate of  meters per jump.
# The second kangaroo starts at location  and moves at a rate of  meters per jump.
# You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES, otherwise return NO.
#
# For example, kangaroo  starts at  with a jump distance  and kangaroo  starts at  with a jump distance of . After one jump, they are both at , (, ), so our answer is YES.
#
# Function Description
#
# Complete the function kangaroo in the editor below. It should return YES if they reach the same position at the same time, or NO if they don't.
#
# kangaroo has the following parameter(s):
#
# x1, v1: integers, starting position and jump distance for kangaroo 1
# x2, v2: integers, starting position and jump distance for kangaroo 2
# Input Format
#
# A single line of four space-separated integers denoting the respective values of , , , and .
#
# Constraints
#
# Output Format
#
# Print YES if they can land on the same location at the same time; otherwise, print NO.
#
# Note: The two kangaroos must land at the same location after making the same number of jumps.
#
# Sample Input 0
#
# 0 3 4 2
# Sample Output 0
#
# YES
# Explanation 0
#
# The two kangaroos jump through the following sequence of locations:
#
# image
#
# From the image, it is clear that the kangaroos meet at the same location (number 12 on the number line) after same number of jumps (4jumps), and we print YES.

def kangaroo(x1, v1, x2, v2):
    for i in range(10000):
        if ((x1 + v1) == (x2 + v2)):
            return "YES"
        x1 += v1
        x2 += v2
    return "NO"


x1 = (0)
v1 = (3)
x2 = (4)
v2 = (2)
print(kangaroo(x1,v1,x2,v2))

