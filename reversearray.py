"""An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index, (where ), that can be referenced as (you may also see it written as

).

Given an array,
, of

integers, print each element in reverse order as a single line of space-separated integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Input Format

The first line contains an integer,
(the number of integers in ).
The second line contains space-separated integers describing

.

Constraints"""
def reverseArray(a):
    start = 0
    end = len(a)-1
    while start < end :
        a[start],a[end] = a[end],a[start]
        start += 1
        end -= 1
    return a