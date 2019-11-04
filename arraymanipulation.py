"""Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each of the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in your array.

For example, the length of your array of zeros $n=10$. Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of $k$ between the indices $a$ and $b$ inclusive:

 1 2 3  4  5 6 7 8 9 10  <---index
[0,0,0, 0, 0,0,0,0,0, 0]
[3,3,3, 3, 3,0,0,0,0, 0]
[3,3,3,10,10,7,7,7,0, 0]
[3,3,3,10,10,8,8,8,1, 0]

The largest value is 10 after all operations are performed.
Sample Input

5 3
1 2 100
2 5 100
3 4 100

Sample Output

200
"""
# def arrayManipulation(n, queries):
#     zeros_list = []
#     highest_element = 0
#     zeros_list = n * zeros_list
#     for query in queries:
#         for index in range(query[0]-1,query[1]):
#             zeros_list[index] += query[2]
#
#     return highest_element


# def get_highest(n, queries):
#     l = [0 for each in range(n)]
#     for each in queries:
#         j = each[0] - 1
#         for i in range(each[1])[j:]:
#             l[i] += each[2]
#     return max(l)

  # zeros_list = [0]
  #   highest_element = 0
  #   zeros_list = n * zeros_list
  #   for query in queries:
  #       for index in range(query[0]-1,query[1]):
  #           zeros_list[index] += query[2]
  #           if highest_element < zeros_list[index]:
  #               highest_element = zeros_list[index]
  #   return highest_element
# def arrayManipulation(n, queries):
#     zeros_list = [0]
#     highest_element = 0
#     zeros_list =n * zeros_list
#     m = 0
#
#     for index in range(queries[m][0],queries[m][1]+1):
#         zeros_list[index-1] += queries[m][2]
#         print(index)
#         if index  == queries[m][1]:
#             m += 1
#         print(zeros_list)
#         if highest_element < zeros_list[index]:
#             highest_element = zeros_list[index]
#     return highest_element
# n, inputs = [int(n) for n in input().split(" ")]
n = 10
m = 3
inputs = [[1,5,3],[4,8,7],[1,9,1]]
list = [0]*(n + 1)
for each in inputs:
    x, y, incr = each

    list[x-1] += incr
    if((y)<=len(list)): list[y] -= incr;
    print(list)
max = x = 0
for i in list:
   x=x+i
   if(max<x): max=x;
print(max)
                                                    