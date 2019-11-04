def get(keyboard,drive,cost):
    spent = -1
    for k in keyboard:
        for d in drive:
            cnt = k + d
            if(cnt <= cost and cnt > spent):
                spent = cnt
    return spent


keyboard = [2,5,4]
drive = [10,3,4]
cost = 10
print(get(keyboard,drive,cost))
