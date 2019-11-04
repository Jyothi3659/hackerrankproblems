def get(keyboard,drive,cost):
    spent = -1
    for k in keyboard:
        for d in drive:
            cnt = k + d
            if(cnt <= cost and cnt > spent):
                spent = cnt
    return spent


keyboard = [-10,-30,10]
drive = [-20,40,-10]
cost = 15
print(get(keyboard,drive,cost))
