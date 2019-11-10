def catMouse(x, y, z):
    catA = x - z
    catB = y - z
    if catA < 0:
        catA = -(catA)
    if catB < 0:
        catB = -(catB)
    if catA < catB:
        return 'Cat A'
    elif catA > catB:
        return 'Cat B'
    else:
        return 'Mouse C'


x = 4
y = 3
z = 5
print(catMouse(x,y,z))
