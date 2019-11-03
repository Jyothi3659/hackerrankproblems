def bonAppetit(bill, k, b):
    count=0
    for i in range(len(bill)):
        if(i!=k):
            count+=bill[i]
    pay = count//2
    if(pay != b):
        print(b-pay)
    else:
        print("Bon Appetit")


bill = (4,1)
k = (3,10,2,9)
b = (7)
bonAppetit(bill,k,b)