def formingamagicsquare(s):
    data = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
           ]
    t = []
    for i in data:
        res = 0
        for j, k in zip(i, s):
            for x, y in zip(j, k):
                res += max([x, y]) - min([x, y])
        t.append(res)
    return min(t)


s = [[4,9,2],[3,5,7],[8,1,5]]
print(formingamagicsquare(s))


