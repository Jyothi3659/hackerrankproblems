def divisibleSumPairs(k, ar):
    count=0
    for i in range(len(ar)):
        for j in range(i+1,len(ar)):
            if(ar[i]+ar[j])%k==0:
                count+=1
    return count


k = 3
ar=[1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(k,ar))


