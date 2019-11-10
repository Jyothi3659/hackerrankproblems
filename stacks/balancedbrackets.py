def isBalanced(s):
    stack = []
    balanced_dict = {'}':'{',']':'[',')':'('}
    for each in s:
        if not stack:
            stack.append(each)
        elif each not in balanced_dict:
            stack.append(each)
        elif balanced_dict[each] == stack[-1]:
            stack.pop()
        else:
            stack.append(each)
    if stack:
        return 'NO'
    else:
        return 'YES'

#     balanced_dict = {'{':'}','(':')','[':']'}
#     j = -1
#     flag = None
#     for i in range(len(s)//2):
#         # print(i)
#         # print(j)
#         if i -j !=0:
#             if balanced_dict[s[i]] == s[j]:
#                 flag = True
#                 j -= 1
#             else:
#                 # print('hjkyvd')
#                 flag = False
#                 break
#         elif i - j >= -1:
#             break
#     if flag is True:
#         return 'YES'
#     else:
#         return 'NO'
# print(isBalanced('{{[[(())]]}}'))
# print(isBalanced('{[(])}'))