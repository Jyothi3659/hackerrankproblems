# # """Objective
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given a base-
# integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in
#
# 's binary representation.
#
# Input Format
#
# A single integer,
#
# .
#
# Constraints
#
# Output Format
#
# Print a single base-
# integer denoting the maximum number of consecutive 's in the binary representation of
#
# .
#
# Sample Input 1
#
# 5
#
# Sample Output 1
#
# 1
#
# Sample Input 2
#
# 13
#
# Sample Output 2
#
# 2
#
# Explanation
#
# Sample Case 1:
# The binary representation of
# is , so the maximum number of consecutive 's is
#
# .
#
# Sample Case 2:
# The binary representation of
# is , so the maximum number of consecutive 's is ."""
def binary_func(n):
    binary_string = bin(n).replace("0b", "")
    previous = binary_string[0]
    final_count = 0
    count = 0
    print(binary_string)
    for each in binary_string:
        if (each != 0 and count == 0):
            count += 1
            previous = each
            print(count)
            if final_count < count:
                final_count = count
        elif (each != 0 and previous == each):
            previous = each
            count += 1
            print(count)
            if final_count < count:
                final_count = count
        else:
            previous = each
            count = 0
    return final_count
print(binary_func(8))