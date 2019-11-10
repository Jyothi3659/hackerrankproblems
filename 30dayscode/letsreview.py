# def ind(t):
#     str = t
#     for i in range(0,len(str)):
#         if (i % 2 == 0):
#             print(str[i],end="")
#     for i in range(0,len(str)):
#         if (i % 2 != 0):
#             print(str[i],end="")
#
#
# t = 'pythonisaprogramminglaunguage'
# ind(t)


N = int(input())

for i in range(0, N):

    string = input()

    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end='')

    print(" ", end='')

    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end='')

    print("")



