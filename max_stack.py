# n = int(input())
# queries = []
# for each in range(n):
#     queries.append(list(map(int,input().rstrip().split())))
import pdb
def stackfunc(queries):
    stacklist = []
    max = None
    pdb.set_trace()
    l = []
    for each in queries:
        if each[0] == 1:
            if max is None:
                max = each[1]
            elif each[1] > max:
                max = each[1]
            stacklist.append([each[1], max])
        elif each[0] == 2:
            stacklist.pop()
            if stacklist:
                max = stacklist[-1][1]
            else:
                max = None
        else:
            l.append(stacklist[-1][1])
    return l
#
#
# class Stack():
#     def init(self):
#         self.items=[]
#     def size(self):
#         return len(self.items)
#     def isEmpty(self):
#         return self.items==[]
#     def pop(self):
#         return self.items.pop()
#     def push(self,item):
#         self.items.append(item)
#     def peek(self):
#         return self.items[len(self.items)-1]

# N=int(input())
# s1=Stack()
# curMax=Stack()
# for i in range(N):
#     query=list(map(int,input().split()))
#     if(query[0]==1):
#         cur=query[1]
#         if(curMax.isEmpty() !=True) :
#             if(curMax.peek()<=cur):
#                 curMax.push(cur)
#             else:
#                 curMax.push(cur)
#                 s1.push(cur)
#     elif(query[0]==2):
#         if((s1.isEmpty() and s1.isEmpty()) != True):
#             if(s1.peek()==curMax.peek()):
#                 curMax.pop()
#                 s1.pop()
#     elif(query[0]==3):
#         print(curMax.peek())