def timeConversion(s):
    time = s.split(":")
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    time = ':'.join(time)
    return str(time[:-2])


s = ("10:40:45PM")
print(timeConversion(s))
