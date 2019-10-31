def repeatedString(s, n):
    repititions = 0
    count = 0
    for each in range(len(s)):
        if s[each] == 'a':
            count += 1
    repititions = n // len(s)
    count = count * repititions
    l = n%len(s)
    for i in range(l):
        if s[i] == 'a':
            count += 1
    return count
s = 'aba'
print(repeatedString(s,10))