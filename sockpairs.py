def sockMerchant(n, ar):
    ar.sort()
    previous = ar[0]
    count = 0
    pairs = 0
    for each in range(len(ar)):
        if previous != ar[each]:
            previous = ar[each]
            pairs += count // 2
            count = 1
        elif each +1 == len(ar):
            count += 1
            pairs += count // 2
        else :
            count += 1
            previous = ar[each]

    return pairs


n = [9]
ar = [1,2,3,5,5,4,9,9,5]
print(sockMerchant(n,ar))
