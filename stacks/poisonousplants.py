# import pdb
# def poisonousPlants(plants):
#     pdb.set_trace()
#     flag = True
#     day = 0
#     while (flag):
#         flag = False
#         i = -1
#         while(i > -len(plants)):
#             if plants[i] > plants[i - 1]:
#                 plants.pop(i)
#                 flag = True
#             else:
#                 i -= 1
#         if flag:
#             day += 1
#     print(day)
#     return day
# def poisonousPlants(p):
#     flag = False
#     previous = None
#     count = 1
#     while count < 7:
#         for each in range(len(p)):
#             if previous == None:
#                 previous = p[each]
#             else:
#                 if p[each] > previous:
#                     previous = p[each]
#                     p.remove(p[each])
#                     flag = True
#                 else:
#                     previous = p[each]
#         count += 1
class Plant:
    def __init__(self, pesticide, days):
        self.pesticide = pesticide
        self.days = days


def solvePlants(a):
    stack = []
    maxDaysAlive = 0

    for pesticide in a:
        daysAlive = 0
        while stack and pesticide <= stack[-1].pesticide:
            daysAlive = max(daysAlive, stack.pop().days)

        if not stack:
            daysAlive = 0
        else:
            daysAlive += 1

        maxDaysAlive = max(maxDaysAlive, daysAlive)

        stack.append(Plant(pesticide, daysAlive))

    print(maxDaysAlive)


# def main():
#     N = input()
#
#     numbers = map(int, raw_input().split())
#
#     solvePlants(numbers)
#
#
# if __name__ == '__main__':
#     main()