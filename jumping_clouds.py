def jumpingOnClouds(c):
    n = 7
    i = 0
    jumps = 0
    try :
        while i < n-1:
            if c[i+2] == 1 or i + 2 >= n:
                i += 1
                jumps += 1
            else :
                i += 2
                jumps += 1
    except IndexError:
        i += 1
        jumps += 1
    return jumps
print(jumpingOnClouds([0,0,1,0,0,0,0]))