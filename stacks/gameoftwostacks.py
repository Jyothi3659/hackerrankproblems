def twoStacks(x, a, b):
    moves = 0
    i = j  = total = 0
    while total+ a[i] < x and i < len(a):
        total += a[i]
        moves += 1
        i += 1
    while total + b[j] < x and j < len(b):
        total += b[j]
        moves += 1
        j += 1
        while total > x:
            moves -= 1
            total -= a[i]
    return moves



