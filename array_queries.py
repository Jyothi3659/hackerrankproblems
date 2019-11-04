# N = int(input())
# A = []
# result = 0
# for each in range(N):
#     A.append(int(input()))
A = [1,2,3,4,5,6,7,8]
M = [[1,2,4],[2,3,5],[1,4,7],[2,1,4]]
N = 8
# def resultingarray(N,M,A):
#     for each in M:
#         if each[0] == 1:
#             a = A[each[1]-1:each[2]]
#             del A[each[1]-1:each[2]]
#             A = a + A
#         else:
#             a = A[each[1]-1:each[2]]
#             del A[each[1]-1:each[2]]
#             A = A + a
#     if A[0] < A[N-1]:
#         result = A[N-1] - A[0]
#     else:
#         result = A[0] - A[N-1]
#     return result
# for each in range(N):
#     A.append(each+1)
def resultingarray(n,m,a):
    for each in m:
        if each[0] == 1:
            if ((each[1]-2) - 0) < (each[2] - each[1]):
                s = a[0 : each[1]-1]
                del a[0 : each[1]-1]
                print(a)
                a = a + s
            else:
                print(a)
                a = a[each[1] - 1:each[2]]
                del a[each[1]-1:each[2]]
                print(a)
        else:
            if (len(a) - each[2]+1) < (each[1]-1 - each[2]-1):
                s = a[-1 : each[2]-2]
                del a[0 : each[2]-2]
                a = a + s
            else:
                a = a[each[2]+1 - 1:each[2]]
                del a[each[1]-1:each[2]]
    # if a[0] < a[-1]:
    #     result = a[-1] - a[0]
    # else:
    #     result = a[0] - a[-1]
    # print(a)
    # return result
print(resultingarray(N,M,A))
